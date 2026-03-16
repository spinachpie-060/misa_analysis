import re
import sys
import argparse
import os  # ファイル名操作のために追加
from Bio import SeqIO

def find_minimal_motif(motif):
    for i in range(1, len(motif) + 1):
        sub = motif[:i]
        if sub * (len(motif) // i) == motif:
            return sub
    return motif

def detect_ssrs(seq, motifs, min_unit, max_unit):
    results = []
    # unit_sizeのループ範囲を常に1からmax_unitまでにし、後で正規化後にフィルタリング
    for unit_size in range(1, max_unit + 1):
        min_repeats = motifs.get(unit_size)
        if not min_repeats:
            continue
        pattern = re.compile(rf"(([ACGT]{{{unit_size}}})\2{{{min_repeats - 1},}})", re.IGNORECASE)
        for m in pattern.finditer(seq):
            full_ssr = m.group(1)
            raw_motif = m.group(2).upper()
            norm_motif = find_minimal_motif(raw_motif)
            norm_len = len(norm_motif)
            
            # 正規化されたモチーフ長が指定範囲外ならスキップ
            if norm_len < min_unit or norm_len > max_unit:
                continue
            # ホモポリマー（AAAなど）を除外
            if len(set(norm_motif)) == 1:
                continue
                
            start = m.start() + 1
            end = m.end()
            repeat_count = len(full_ssr) // norm_len
            results.append((start, end, norm_motif, repeat_count, f"({norm_motif}){repeat_count}"))
    return results

def write_gff(gff_file, seq_id, seq_len, ssrs):
    with open(gff_file, 'w') as gff:
        gff.write("##gff-version 3\n")
        gff.write(f"##sequence-region {seq_id} 1 {seq_len}\n")
        for i, (start, end, motif, repeat_count, ssr) in enumerate(ssrs, 1):
            feature_type = "microsatellite"
            note = f"{feature_type},{ssr}"
            gff.write(f"{seq_id}\tMISA\t{feature_type}\t{start}\t{end}\t.\t.\t.\tNote={note};ID={seq_id}.{i}\n")

def write_tsv(tsv_file, seq_id, ssrs):
    # すでにファイルが存在する場合は追記モード、新規の場合はヘッダーから
    file_exists = os.path.isfile(tsv_file)
    with open(tsv_file, 'a') as tsv:
        if not file_exists:
            tsv.write("ID\tStart\tEnd\tMotif\tRepeats\tSSR\n")
        for start, end, motif, repeat_count, ssr in ssrs:
            tsv.write(f"{seq_id}\t{start}\t{end}\t{motif}\t{repeat_count}\t{ssr}\n")

def main():
    parser = argparse.ArgumentParser(description="SSR detector with normalized motif filtering")
    parser.add_argument("fasta", help="Input FASTA file")
    parser.add_argument("--min-unit", type=int, default=2, help="Minimum motif size (default: 2)")
    parser.add_argument("--max-unit", type=int, default=6, help="Maximum motif size (default: 6)")
    args = parser.parse_args()

    # 最小反復回数の定義
    motifs = {1: 10, 2: 6, 3: 5, 4: 5, 5: 5, 6: 5}

    # 出力ファイルのベース名を作成
    # 例: input.fasta -> input_u2to6
    base_input = os.path.basename(args.fasta).replace('.fasta', '').replace('.fa', '').replace('.gz', '')
    output_prefix = f"{base_input}_u{args.min_unit}to{args.max_unit}"
    
    tsv_out = f"{output_prefix}.tsv"
    gff_out = f"{output_prefix}.gff"

    # 既存の出力ファイルがある場合は削除してから開始（追記モードのため）
    for f in [tsv_out, gff_out]:
        if os.path.exists(f):
            os.remove(f)

    import gzip
    if args.fasta.endswith('.gz'):
        handle = gzip.open(args.fasta, 'rt')
    else:
        handle = open(args.fasta, 'r')

    for record in SeqIO.parse(handle, "fasta"):
        seq_id = record.id
        seq = str(record.seq).upper()
        ssrs = detect_ssrs(seq, motifs, args.min_unit, args.max_unit)

        if ssrs:
            # 1つのファイルに全配列の結果をまとめる形式に変更
            write_gff_append(gff_out, seq_id, len(seq), ssrs)
            write_tsv(tsv_out, seq_id, ssrs)

def write_gff_append(gff_file, seq_id, seq_len, ssrs):
    file_exists = os.path.isfile(gff_file)
    with open(gff_file, 'a') as gff:
        if not file_exists:
            gff.write("##gff-version 3\n")
        gff.write(f"##sequence-region {seq_id} 1 {seq_len}\n")
        for i, (start, end, motif, repeat_count, ssr) in enumerate(ssrs, 1):
            feature_type = "microsatellite"
            note = f"{feature_type},{ssr}"
            gff.write(f"{seq_id}\tMISA\t{feature_type}\t{start}\t{end}\t.\t.\t.\tNote={note};ID={seq_id}.{i}\n")

if __name__ == "__main__":
    main()

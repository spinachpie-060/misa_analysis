import re
import sys
import argparse
from Bio import SeqIO

def find_minimal_motif(motif):
    for i in range(1, len(motif) + 1):
        sub = motif[:i]
        if sub * (len(motif) // i) == motif:
            return sub
    return motif

def detect_ssrs(seq, motifs, min_unit, max_unit):
    results = []
    for unit_size in range(1, max_unit + 1):  # always check all possible units
        min_repeats = motifs.get(unit_size)
        if not min_repeats:
            continue
        pattern = re.compile(rf"(([ACGT]{{{unit_size}}})\2{{{min_repeats - 1},}})", re.IGNORECASE)
        for m in pattern.finditer(seq):
            full_ssr = m.group(1)
            raw_motif = m.group(2).upper()
            norm_motif = find_minimal_motif(raw_motif)
            norm_len = len(norm_motif)
            if norm_len < min_unit or norm_len > max_unit:
                continue  # filter by normalized motif length
            if len(set(norm_motif)) == 1:
                continue  # skip homopolymers like AAA, TTT
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
    with open(tsv_file, 'w') as tsv:
        tsv.write("ID\tStart\tEnd\tMotif\tRepeats\tSSR\n")
        for i, (start, end, motif, repeat_count, ssr) in enumerate(ssrs, 1):
            tsv.write(f"{seq_id}\t{start}\t{end}\t{motif}\t{repeat_count}\t{ssr}\n")

def main():
    parser = argparse.ArgumentParser(description="SSR detector with normalized motif filtering")
    parser.add_argument("fasta", help="Input FASTA file")
    parser.add_argument("--min-unit", type=int, default=2, help="Minimum motif size (default: 2)")
    parser.add_argument("--max-unit", type=int, default=6, help="Maximum motif size (default: 6)")
    args = parser.parse_args()

    motifs = {1: 10, 2: 6, 3: 5, 4: 5, 5: 5, 6: 5}

    import gzip

    # 入力ファイルを開く（.gz 対応）
    if args.fasta.endswith('.gz'):
        handle = gzip.open(args.fasta, 'rt')
    else:
        handle = open(args.fasta, 'r')

    for record in SeqIO.parse(handle, "fasta"):
        seq_id = record.id
        seq = str(record.seq).upper()
        ssrs = detect_ssrs(seq, motifs, args.min_unit, args.max_unit)

        if ssrs:
            write_gff(f"{seq_id}.gff", seq_id, len(seq), ssrs)
            write_tsv(f"{seq_id}.tsv", seq_id, ssrs)

if __name__ == "__main__":
    main()

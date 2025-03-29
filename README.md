# MISA-like SSR検出ツール（学生向けチュートリアル）

このリポジトリには、FASTA形式のDNA配列からマイクロサテライト（SSR）を検出するPythonスクリプトが含まれています。
出力はGFF3およびTSV形式で得られます。

---

## ✨ このスクリプトができること

- 完全一致のSSR（繰り返し配列）を検出
- モチーフ（繰り返し単位）を**最短の単位に正規化**
- ホモポリマー（例：AAA、TTTT）を自動的に除外
- 繰り返し単位長（モチーフ長）でフィルタリングが可能

---

## ⚙️ 動作環境

- Python 3.6 以上
- Biopython ライブラリ

### 🔧 インストール方法
```bash
pip install biopython
```

---

## 📁 リポジトリの構成

| ファイル名 | 説明 |
|------------|------|
| `misa_like_normalized_filtered.py` | SSR検出用Pythonスクリプト |
| `SOL_chr6.fa.gz` | 解析用FASTAファイル（圧縮形式） |
| `example_output/` | 出力例（.tsv, .gff） |

---

## ▶️ 実行方法

### 基本的な使い方：
```bash
python misa_like_normalized_filtered.py SOL_chr6.fa.gz
```

### 繰り返し単位の長さを指定（例：3～6塩基）
```bash
python misa_like_normalized_filtered.py SOL_chr6.fa.gz --min-unit 3 --max-unit 6
```

---

## 🧪 出力形式

- `.tsv`：SSRリスト（開始/終了位置、モチーフ、繰り返し数）
- `.gff`：ゲノムブラウザ用アノテーション形式

### 出力例（TSV）
```
ID	Start	End	Motif	Repeats	SSR
Chr6	100	120	TTA	7	(TTA)7
```

---

## 🎓 実習課題例

- 自分の配列を使ってSSRを検出してみよう
- `--min-unit` や `--max-unit` を変更して結果を比較
- 出力された `.gff` を IGV などのゲノムブラウザで表示

---

## 🇬🇧 English version (optional)

This repository contains a Python script to detect perfect SSRs (microsatellites) in DNA sequences provided in FASTA format. The output includes normalized motifs (shortest repeat units), skips homopolymers, and exports to TSV and GFF3.

### Requirements
- Python 3.6+
- Biopython: `pip install biopython`

### Run Example:
```bash
python misa_like_normalized_filtered.py SOL_chr6.fa.gz --min-unit 3 --max-unit 6
```

### Output:
- `*.tsv`: list of SSRs
- `*.gff`: annotations for genome browsers

---

ご不明点があれば、担当教員またはリポジトリのIssueにてご連絡ください。

Happy sequencing! 🚀


# MISA-like SSR検出ツール（学生向けチュートリアル）

このリポジトリには、FASTA形式のDNA配列からマイクロサテライト（SSR）を検出するPythonスクリプト "misa_like_normalized_filtered.py" が含まれています。
出力はGFF3およびTSV形式で得られます。

---

## ✨ "misa_like_normalized_filtered.py" ができること

- 完全一致のSSR（繰り返し配列）を検出
- モチーフ（繰り返し単位）を**最短の単位に正規化**
- ホモポリマー（例：AAA、TTTT）を自動的に除外
- 繰り返し単位長（モチーフ長）でフィルタリングが可能
- `.fa.gz` などの**圧縮FASTAも自動的に解凍して解析可能**（Biopython使用）

---

## ⚙️ 動作環境

- Python 3.6 以上
- Biopython ライブラリ

### 🔧 インストール方法
```bash
pip install biopython

```
### 🔧 実習終了後に、アンインストールしたい場合
```bash
pip uninstall biopython

```
すると、以下のような確認メッセージが表示されます：

Found existing installation: biopython 1.79
Uninstalling biopython-1.79:
  Would remove:
    /usr/local/lib/python3.10/site-packages/Bio/
    ...
Proceed (Y/n)?

✅ y を押せば削除されます。

---

## 📁 リポジトリの構成

| ファイル名 | 説明 |
|------------|------|
| `misa_like_normalized_filtered.py` | SSR検出用Pythonスクリプト |
| `Zea_chr1_region01.fa.gz` ~ `Zea_chr1_region10.fa.gz` | トウモロコシChr1の異なる10領域（各1Mbp） |
| `Chr6.tsv` | SSR検出結果（タブ区切りテーブル） |
| `Chr6.gff` | SSR検出結果（ゲノムブラウザ表示用GFF3） |
| `README.md` | この説明ファイル |

---

## 💾 ダウンロード・解凍の方法（学生向け）
# curl を使う場合（macユーザー）：
```bash
curl -L -o misa_analysis.zip https://github.com/spinachpie-060/misa_analysis/archive/refs/heads/main.zip

```

# wget を使う場合（ubuntuユーザー）：
```bash
wget -O misa_analysis.zip https://github.com/spinachpie-060/misa_analysis/archive/refs/heads/main.zip

```

ダウンロード後、次のように解凍：解凍すると、フォルダ "misa_analysis-main" が作られる
```bash
unzip misa_analysis.zip

```

フォルダに移動：
```bash
cd misa_analysis-main  

```

フォルダの中を確認する：フォルダ内に解析に使うファイル一式があるのか確認する。
```bash
ls misa_analysis-main 

```

⸻

### 📦 `.fa.gz` を解凍したい場合
```bash
gunzip Zea_chr1_region01.fa.gz
```
※ ただし、解凍しなくてもスクリプトはそのまま実行可能です。

---

## ▶️ 実行方法：　カレントディレクトリを解凍後のダウンロードフォルダ内に設定してから実行

### 基本的な使い方（例：トウモロコシChr1の1領域に対して）：
```bash
python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz
```

### 繰り返し単位の長さを指定（例：3～6塩基）
```bash
python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz --min-unit 3 --max-unit 6
```

※ `.fa.gz` のままで実行できます（Biopythonが自動で解凍します）

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
- 10領域を一気に解析させるスクリプトを作って実行してみよう：ヒント for文（繰り返し処理） https://abundant-dill-cf4.notion.site/1c4d8ba9f8e2804f96a2e28f0c7c700b
- 10領域の中で最もSSRが多い領域を比較・考察してみよう
- 出力された `.gff` を IGV などのゲノムブラウザで表示

---

## 💡 Linuxやターミナルが初めての方へ（Notion教材）

初めてLinuxやターミナルを使う方向けに、以下のページで解説をしています。
インストール、基本操作、ファイル操作などを丁寧に紹介しています。

👉 [学生実習：初めてのLinuxを使ったバイオインフォマティクス（Notion）](https://abundant-dill-cf4.notion.site/Linux-1c2d8ba9f8e28081aa61f9377804f109)

実行に入る前に一度目を通しておくと安心です。

---

## 🇬🇧 English version (optional)

This repository contains a Python script to detect perfect SSRs (microsatellites) in DNA sequences provided in FASTA format. The output includes normalized motifs (shortest repeat units), skips homopolymers, and exports to TSV and GFF3.

### Requirements
- Python 3.6+
- Biopython: `pip install biopython`

### Run Example:
```bash
python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz --min-unit 3 --max-unit 6
```

### Output:
- `*.tsv`: list of SSRs
- `*.gff`: annotations for genome browsers

---

ご不明点があれば、担当教員またはリポジトリのIssueにてご連絡ください。

Happy sequencing! 🚀


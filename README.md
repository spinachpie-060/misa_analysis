# MISA-like SSR検出ツール（Codespaces 版・学生向けチュートリアル）

このリポジトリは **GitHub Codespaces** を使って、  
ブラウザ上で **Linux 操作・Python スクリプト実行・SSR（マイクロサテライト）解析** を体験するための教材です。

本実習では以下の基礎を学びます。

- GitHub の基本操作
- Codespaces の起動と利用
- Linux ターミナル操作
- Python スクリプトの実行
- DNA 配列からの SSR 検出
- 出力結果の確認と考察

Codespaces を使うため、**自分の PC に Python や Linux をインストールする必要はありません。**

---

# 🌐 はじめに：Codespaces の使い方（必ず読む）

## 1. 教材リポジトリを開く

以下のページにアクセスします。

https://github.com/spinachpie-060/misa_analysis

---

## 2. リポジトリを自分の GitHub アカウントにコピー

右上の

Use this template

をクリックし、

Create a new repository

を選び、自分の GitHub アカウントにコピーします。

※ 先生のリポジトリを直接編集することはありません。

---

## 3. Codespaces を起動する

自分の作成したリポジトリを開き、

Code
↓
Codespaces
↓
Create codespace on main

をクリックします。

すると **ブラウザ上で VS Code が起動**します。

---

## 4. ターミナルを開く

VS Code メニュー

Terminal → New Terminal

またはショートカット

Ctrl + Shift + `

---

# ⚙️ 必要ライブラリについて

この教材では **Biopython** を使用します。

通常は次のコマンドでインストールします。

pip install biopython

（同じ Codespace では1回だけでOK）

---

# 📁 リポジトリの構成

| ファイル | 説明 |
|---|---|
| misa_like_normalized_filtered.py | SSR検出用Pythonスクリプト |
| Zea_chr1_region01.fa.gz ～ Zea_chr1_region10.fa.gz | トウモロコシChr1の10領域 |
| Chr6.tsv / Chr6.gff | SSR検出結果の例 |
| README.md | この説明 |
|manual_misa_like_normalized_filtered.md|misa_like_normalized_filtered.py の使い方解説|
| analysis_examples.md | 出力結果の解析チュートリアル |

---

# ▶️ 実行方法

## 1. ファイル確認

ls -1

---

## 2. SSR検出（基本）

python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz

成功すると

1:1-1000000.tsv
1:1-1000000.gff

が生成されます。

---

## 3. モチーフ長を指定

例：3〜6塩基

python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz --min-unit 3 --max-unit 6

---

## 4. gzip を解凍する場合（通常不要）

gunzip Zea_chr1_region01.fa.gz

`.fa.gz` のまま実行できます。

---

# 🧪 出力形式

### TSV

ID	Start	End	Motif	Repeats	SSR
1:1-1000000	100	120	TTA	7	(TTA)7

### GFF

1:1-1000000	MISA	microsatellite	100	120	.	.	.	Note=microsatellite,(TTA)7;ID=1:1-1000000.1

GFF は IGV などのゲノムブラウザで可視化できます。

---

# 🎓 実習課題

## 課題1

Zea_chr1_region01.fa.gz

を解析し、生成された `.tsv` と `.gff` を確認せよ。

---

## 課題2

10領域すべてを解析する Bash スクリプトを書きなさい。

ヒント：

for f in Zea_chr1_region*.fa.gz
do
python misa_like_normalized_filtered.py “$f”
done

---

## 課題3

モチーフ長を変えて比較

例

–min-unit 2 –max-unit 3
–min-unit 4 –max-unit 6

---

## 課題4

出力された TSV を Linux コマンドで解析せよ。

analysis_examples.md

を参考にすること。

---

# 🛑 Codespaces の終了

作業が終わったら

VS Code 下部

Codespaces
↓
Stop Current Codespace

※ブラウザを閉じただけでは停止しません。

---

# 💡 Linux初心者向け教材

https://abundant-dill-cf4.notion.site/Linux-1c2d8ba9f8e28081aa61f9377804f109


⸻




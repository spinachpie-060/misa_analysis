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

※ 以降、自分の GitHub アカウントにコピーしたリポジトリを操作します。
従って、"spinachpie-060" のリポジトリ（misa_analysis）を直接編集することはありません。

---

# 📁 リポジトリの構成

| ファイル | 説明 |
|---|---|
| README.md | この説明 |
| GitHub アカウントの作り方（学生向けガイド）.md | これを読んでアカウントを作ってください |
| 🐚 シェル（Shell）とは？.md | シェルに関する説明。まず、最初に、これを読んでください。|
| 🐧 初心者向け Linux コマンド入門.md | Linuxの超基本コマンドの解説。次に、読むべきはこれ！ |
| 🐚 シェルスクリプト初心者ガイド.md | 簡単なプログラム作成から実行まで。最後に、これを読んでください。 |
| manual_misa_like_normalized_filtered.md |misa_like_normalized_filtered.v2.py の使い方解説 |
| misa_like_normalized_filtered.v2.py | SSR検出用Pythonスクリプト |
| Zea_chr1_region01.fa.gz ～ Zea_chr1_region10.fa.gz | トウモロコシChr1の10領域 |
| Chr6.tsv / Chr6.gff | SSR検出結果の例 |
| analysis_examples.md | 出力結果の解析チュートリアル |
| IGV (Integrative Genomics Viewer) で SSR検出結果を確認するマニュアル.md | ゲノムブラウザーIGVを使って、出力結果を確認しよう |

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

通常は次のコマンドでインストールしますが、リポジトリをコピーすると自動でインストールされるように設定したので、今回は以下の操作は不要です。

```
pip install biopython # 同じ Codespace では1回だけでOK
```

---

# Linux ターミナル操作

**以下の順で、ファイルにある課題に取り組んで、Linux ターミナル操作に慣れよう。**

- 🐚 シェル（Shell）とは？.md
- 🐧 初心者向け Linux コマンド入門.md
- 🐚 シェルスクリプト初心者ガイド.md

---

# 🎓 実習課題
ここからは、Python スクリプト **misa_like_normalized_filtered.v2.py** を使って、
大きなDNA配列ファイル（FASTA）から、SSRを同定する操作を行います。
**manual_misa_like_normalized_filtered.md** を参考にして、以下の課題に取り組んでください。

## 課題1

Zea_chr1_region01.fa.gz ~ Zea_chr1_region10.fa.gz から、FASTAファイルを1つ選び、

**misa_like_normalized_filtered.v2.py** を用いて解析し（オプションを設定しない）、
生成された `.tsv` と `.gff` を確認せよ。

**同じ班のメンバー間で、異なるファイルを選んでください。**

---

## 課題2

Zea_chr1_region01.fa.gz ~ Zea_chr1_region10.fa.gz から、
FASTAファイルを1つ選び（課題1と同じでOK）、
**異なる2通りのモチーフ長条件を指定**して、**misa_like_normalized_filtered.v2.py** を用いて解析し、
生成された `.tsv` と `.gff` を確認せよ。

---

## 課題3

**analysis_examples.md** の手順に従って、
出力された TSV を Linux コマンドで解析せよ。

---

## 課題4

Zea_chr1_region01.fa.gz ~ Zea_chr1_region10.fa.gz の全てを、
**misa_like_normalized_filtered.v2.py** を用いて **一括で解析** する Bash スクリプトを作成し、実行しなさい。

**シェルスクリプト初心者ガイド** にヒントがあります。 **for 文** が鍵になります。

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




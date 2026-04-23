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

## 2. 教材リポジトリを自分の GitHub アカウントに複製（Fork）**

- 教材ページ（ [https://github.com/spinachpie-060/misa_analysis](https://github.com/spinachpie-060/misa_analysis) ）にアクセスします。

- 画面右上にある **[Fork]** ボタンをクリックします。

- 設定画面が表示されたら、そのまま右下の **[Create fork]** をクリックしてください。

      * これで、ご自身のアカウント内に `(ユーザー名)/misa_analysis` というコピーが作成されます。

      ※ 以降の作業は、必ず**自分自身のアカウントに作成されたリポジトリ**で行ってください。

---

# 📁 リポジトリの構成

**本リポジトリの構成は以下の通りです。**

```text
.
├── README.md               # 本ファイル（プロジェクト概要）
├── Chr6.gff                # ゲノムアノテーションファイル
├── Chr6.tsv                # SSR検出結果等のデータ
├── misa_like_normalized_filtered.v2.py # 解析用メインスクリプト
├── sample1.txt # ファイル操作の練習用ファイル
├── sample2.txt # ファイル操作の練習用ファイル
├── fastas/                 # トウモロコシのゲノム配列データ（分割された Fasta 形式）
│   ├── Chr01_pos01.fasta.gz
│   ├── ...
│   └── Chr10_pos10.fasta.gz
└── チュートリアル/          # 学習用マニュアル類
    ├── 0.GitHub アカウントの作り方...          # これを読んでアカウントを作ってください 
    ├── 1.🐚 シェル（Shell）とは？...          # シェルに関する説明。まず、最初に、これを読んでください。
    ├── 2.🐧 初心者向け Linux コマンド入門...          #  Linuxの超基本コマンドの解説。次に、読むべきはこれ！ 
    ├── 3.🐚 シェルスクリプト初心者ガイド...          # 簡単なプログラム作成から実行まで。
    ├── 4.manual_misa_like_normalized_filtered.md          # misa_like_normalized_filtered.v2.py の使い方解説
    ├── 5.analysis_examples.md          # 出力結果の解析チュートリアル
    ├── 6.IGV (Integrative Genomics Viewer) で確認するマニュアル...          # ゲノムブラウザーIGVを使って、出力結果を確認しよう
    └── 7.🖥️ Windows PC に WSL2 と Ubuntu をインストールする手順...          # Windows PCでLinuxを使い場合
```

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

ディレクトリ **fastas** に格納されたFASTAファイル
**Chr01_pos01.fasta.gz** ~ **Chr10_pos10.fasta.gz** から、1つ選び、

**misa_like_normalized_filtered.v2.py** を用いて解析し（オプションを設定しない）、
生成された `.tsv` と `.gff` を確認せよ。

**同じ班のメンバー間で、異なるファイルを選んでください。**

---

## 課題2

ディレクトリ **fastas** に格納されたFASTAファイル
**Chr01_pos01.fasta.gz** ~ **Chr10_pos10.fasta.gz** から、
1つ選び（課題1と同じでOK）、
**異なる2通りのモチーフ長条件を指定**して、**misa_like_normalized_filtered.v2.py** を用いて解析し、
生成された `.tsv` と `.gff` を確認せよ。

さらに、2つの検索条件の間で、検出された SSR の数に、違いがあるのか確認する。
（**analysis_examples.md** に具体的な方法を示しています。）

---

## 課題3

特定の染色体の10領域の全てを、
**misa_like_normalized_filtered.v2.py** を用いて **一括で解析** する Bash スクリプトを作成し、実行しなさい。
**シェルスクリプト初心者ガイド** にヒントがあります。 **for 文** が鍵になります。
オプションは、自由に設定してください。ただし、SSRが検出されない厳しい条件は採用しないように注意すること。

---

## 課題4

課題3の解析によって、出力された10領域のTSVファイルから、2つ（2領域）選んで、「検出された SSR の数」、「モチーフ頻度」、「繰り返し回数の分布」、「繰り返し回数が多いSSRの抽出」、「SSRの位置分布」を調査し、両者を比較しなさい。
（**analysis_examples.md** に具体的な方法を示しています。）

---

## 課題5

課題3で解析した10領域それぞれの合計SSR数を計算し、染色体上のSSR数の分布をグラフ化しなさい。

（**analysis_examples.md** に具体的な方法を示しています。）

---

## 課題6

今回の課題を通じて出力された出力結果（GFFファイル）を、ゲノムブラウザー（IGV）使って確認してください。
（'6.IGV (Integrative Genomics Viewer) で SSR検出結果を確認するマニュアル.md'に手順が記載されています。）


---

# 🛑 Codespaces の終了

作業が終わったら

VS Code 下部

Codespaces
↓
Stop Current Codespace

※ブラウザを閉じただけでは停止しません。

⸻




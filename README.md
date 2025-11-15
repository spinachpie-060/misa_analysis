MISA-like SSR検出ツール（Codespaces 版・学生向けチュートリアル）

このリポジトリは、GitHub Codespaces を使って
ブラウザ上で Linux と Python を練習しながら、
FASTA形式のDNA配列からマイクロサテライト（SSR）を検出する実習を行うための教材です。

Codespaces を使うため、自分のPCに何もインストールする必要はありません。

⸻

🌐 はじめに：Codespaces の使い方（必ず読む）

1. リポジトリを自分のGitHubアカウントにコピー（Use this template）

右上の
“Use this template” → “Create a new repository”
をクリックし、自分のアカウントにコピーします。

※ 先生のリポジトリに直接書き込むことはありません。

⸻

2. Codespaces を起動する

自分の作ったリポジトリを開き、
緑色の 「Code」ボタン → Codespaces タブ → “Create codespace on main”
をクリックします。

すると、ブラウザ上で VS Code が起動します。

⸻

3. ターミナルを開く

VS Code（Codespaces）のメニューから：

Terminal → New Terminal

またはショートカット：

Ctrl + Shift + `

これで Codespaces の Linux ターミナルが開きます。

⸻

⚙️ まずやること：Biopython をインストール

Codespaces は軽量環境なので、必要なライブラリは自分で入れます。

ターミナルで：

pip install biopython

（1回だけでOK。同じ Codespace では次回から不要）

⸻

📁 リポジトリの構成

ファイル名	説明
misa_like_normalized_filtered.py	SSR検出用Pythonスクリプト
Zea_chr1_region01.fa.gz ~ Zea_chr1_region10.fa.gz	トウモロコシChr1の10領域（各1Mbp）
Chr6.tsv / Chr6.gff	例としての SSR 検出結果（比較用）
README.md	本チュートリアル

Codespaces 起動後は自動的にこれらのファイルが見えます。

⸻

▶️ 実行方法（Codespaces 内）

1. ファイル一覧を確認

ls -1

misa_like_normalized_filtered.py と
Zea_chr1_region01.fa.gz などのファイルが見えるはずです。

⸻

2. SSR検出を実行（基本）

python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz

成功すると、次のようなファイルが新しく作られます：
	•	1:1-1000000.tsv
	•	1:1-1000000.gff

（配列IDに応じて名前は変わります）

⸻

3. モチーフ長を指定したい場合（例：3〜6塩基）

python misa_like_normalized_filtered.py Zea_chr1_region01.fa.gz --min-unit 3 --max-unit 6


⸻

4. gzip を手動で解凍したい場合（不要だが可能）

gunzip Zea_chr1_region01.fa.gz

※解凍せずに .fa.gz のままでスクリプトは実行できます。

⸻

🧪 出力形式

TSV（表形式）

ID	Start	End	Motif	Repeats	SSR
1:1-1000000	100	120	TTA	7	(TTA)7

GFF（ゲノムブラウザ用）

1:1-1000000	MISA	microsatellite	100	120	.	.	.	Note=microsatellite,(TTA)7;ID=1:1-1000000.1

IGV 等で可視化できます。

⸻

🎓 実習課題

Codespaces 上で、以下の課題に挑戦してみましょう。

✔ 課題1：自分で実行してみる

Zea_chr1_region01.fa.gz のSSRを検出し、
出力された .tsv と .gff を確認せよ。

⸻

✔ 課題2：10領域すべてをループ実行するBashスクリプトを作る

ヒント：

for f in Zea_chr1_region*.fa.gz
do
  python misa_like_normalized_filtered.py "$f"
done


⸻

✔ 課題3：モチーフ長の条件を変えて比較する

例：

--min-unit 2 --max-unit 3
--min-unit 4 --max-unit 6

違いを考察せよ。

⸻

✔ 課題4：出力された GFF を IGV で見てみる

Codespaces で作った GFF をローカルにダウンロードして可視化する。

⸻

🛑 Codespaces の終了方法

作業が終わったら、
VS Code 下部にある「Codespaces ○○」をクリックし：

→ Stop Current Codespace

とすると、計算リソースの消費を止められます。

（コマンドラインの exit では Codespace は止まりません）

⸻

💡 Linux初心者向け教材

Linux の基礎を事前に学びたい場合はこちら：

👉 https://abundant-dill-cf4.notion.site/Linux-1c2d8ba9f8e28081aa61f9377804f109

⸻

🇬🇧 English version (optional)

(省略せず元の英語部分も必要なら付けます)

⸻

必要であれば：
	•	「Codespaces 入門」ページ
	•	「学生用スタートガイド（PDF）」
	•	「スクリプト分解解説ページ」

も作成できますのでお知らせください。

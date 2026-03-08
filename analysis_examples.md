---

# 1. ファイル確認

ls *.tsv

---

# 2. SSR の数を調べる

wc -l 1:1-1000000.tsv

注意：1行目はヘッダー

実際の SSR 数

行数 - 1

---

# 3. モチーフ頻度

cut -f4 1:1-1000000.tsv | tail -n +2 | sort | uniq -c | sort -nr | head

---

# 4. 繰り返し回数の分布

cut -f5 1:1-1000000.tsv | tail -n +2 | sort -n | uniq -c

---

# 5. 繰り返し回数が多い SSR

例：10回以上

awk ‘NR==1 || $5 >= 10’ 1:1-1000000.tsv

---

# 6. SSR の位置分布

cut -f2 1:1-1000000.tsv | tail -n +2 | awk ‘{print int($1/10000)}’ | sort | uniq -c

---

# 7. 複数ファイル比較

for f in *.tsv
do
echo $f
tail -n +2 $f | wc -l
done

---

# 8. 考察

以下について考察してください。

- SSR が多い領域はどこか
- よく出現するモチーフは何か
- 繰り返し回数が大きい SSR はあるか


⸻


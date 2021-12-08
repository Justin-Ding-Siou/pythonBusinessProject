
import csv
import re

# Read text as a string
# 上傳前要改為，news.txt 原檔名
with open("2021_Spring_Test02_Code/news.txt", encoding='utf-8') as f:
  news = f.read()

# print(news)

# 複製原始新聞字串
s = news[0:]

# 移除英文字與數字
en_words_pattern = '[a-zA-Z0-9]+'
en_words = set(re.findall(en_words_pattern, s))
print(f"\n不重複英數字有 {len(en_words)} 個: {en_words}\n")

for w in sorted(en_words, key=lambda x: len(x), reverse=True):
  s = s.replace(w, "")

# 移除標點符號, 只留中文字
chars_to_remove = ' .,：，。、／〔〕（）《》「」\n'
for char in chars_to_remove:
  s = s.replace(char, '')
# print(s)

# import string
# ascii_chars = set(string.printable)  # speeds things up
# char_set = [c for c in set(s) if c not in ascii_chars]

# 轉換成字元集合
char_set = set(s)

# 印出字集, 找出現的順序
sorted_chars = sorted(char_set, key=news.index)
print(f"不重複中文字有 {len(sorted_chars)} 個: {sorted_chars}\n")

# 建構字元字典array 
rows = []

# Using string.count(c)   
for c in sorted_chars: # based on unique words
  n = s.count(c)
  row = [c, n]
  rows.append(row)

# 依出現次數排序
rows_sorted = sorted(rows, key=lambda x: x[1], reverse=True)
# print("\n最常用的5個中文字:", rows_sorted[0:5])

# 存入 csv
import os
path = '2021_Spring_Test02_Code/output'
filename = 'news_word_counts.csv'
filepath = f'{path}/{filename}'
os.makedirs(path, exist_ok= True)

with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
  writer = csv.writer(f)
  writer.writerow(['單字','次數'])          # 寫入標題列
  writer.writerows(rows_sorted)             # 寫入Data列

# Read data
print("\nData Rows ... ")
with open(filepath, 'r', encoding='utf-8-sig') as f:
  csv_reader = csv.reader(f)
  # next(csv_reader) # skip first row

  for row in csv_reader:
    print(row) 
  
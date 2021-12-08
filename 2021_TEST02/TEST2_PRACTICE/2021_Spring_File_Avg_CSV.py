# -*- Coding: utf-8 -*-

import os
import json

# Read credits.txt and create credits dic
infolder = "data"
outfolder = 'output'
filename = 'credits_all.txt'
filepath = os.path.join(infolder, filename)

credits_dict = {} # {course: credits}
# 檔案路徑要改為由 \ = /，注意是在電腦上看的
# 之後上傳後，經由 pycharm確認，改為 filepath
with open('C://Users/Ting/PycharmProjects/pythonBusinessProject/2021_TEST02/TEST2_PRACTICE/data/credits_all.txt', encoding='utf-8') as f: 
    for line in f:
        words = line.strip().split(":") # 去掉每列的 :
        # print(words)
        k = words[0].strip() # 清理字串
        v = words[1].strip() # 清理字串
        credits_dict[k] = int(v) # 轉為字典，且將 words[1] 轉為字典

# print(credits_dict)
# courses = sorted(credits_dict.keys(), key=lambda x: x)
# print(courses)

# Read grades json file
# 之後上傳後，改為 filepath
jsonfile = "grades.json"
jsonpath = os.path.join(infolder, jsonfile)
grade_dict = {}

with open('C://Users/Ting/PycharmProjects/pythonBusinessProject/2021_TEST02/TEST2_PRACTICE/data/grades.json', encoding='utf-8') as f:
  data = f.read()
  grade_dict = json.loads(data)

# print(grade_dict)

# Create credit list
# credits = [credits_dict[c.strip()] for c in cols[1:]]

# Read data row by row
avg_list = []

for k, v in grade_dict.items():   
  total_scores = 0
  total_credits = 0 
  for c, s in v.items():
    if s >= 0:
      total_scores +=  int(s) * credits_dict[c]
      total_credits += credits_dict[c]
  
  avg = int((total_scores/total_credits) * 100) / 100
  # print('{0}: {1:.2f}'.format(k, avg))
  print(f'{k}: {avg}')
  avg_list.append([k, avg])

avg_sorted = sorted(avg_list, key=lambda x: (-x[1], x[0]))
# print(avg_sorted)

print("\nTop 5 students:")
for item in avg_sorted[0:5]:
  print(f'{item[0]}: {item[1]}')

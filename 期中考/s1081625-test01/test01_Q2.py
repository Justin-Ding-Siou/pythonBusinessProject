grade_dict = {'s1081391': {'Finance': 65, 'Chemistry': 95, 'Economics': 65, 'English': 55, 'Accounting': 70}, 's1081112': {'English': 80, 'Data Structures': 60, 'History': 45, 'Calculus': 80, 'Networks': 95}, 's1081147': {'Algorithms': 65, 'Biology': 90, 'Community Service': 95, 'Data Structures': 50, 'Networks': 65}, 's1081204': {'Data Structures': 85, 'Chemistry': 60, 'Community Service': 80, 'Economics': 70, 'Finance': 85}, 's1081254': {'Networks': 85, 'Data Structures': 85, 'Calculus': 65, 'History': 70, 'Biology': 70}, 's1081153': {'Finance': 45, 'Data Structures': 75, 'ROTC service': 75, 'Calculus': 75, 'Accounting': 60}, 's1081201': {'Management': 60, 'Physics': 75, 'Data Structures': 95, 'Biology': 55, 'Chemistry': 55}, 's1081342': {'Management': 40, 'Economics': 60, 'English': 95, 'Networks': 85, 'Calculus': 60}, 's1081172': {'Management': 50, 'Finance': 80, 'ROTC service': 40, 'Economics': 45, 'Data Structures': 45}, 's1081353': {'Algorithms': 95, 'Chemistry': 40, 'Biology': 65, 'Calculus': 40, 'Finance': 95}, 's1081247': {'Physics': 80, 'History': 65, 'Community Service': 55, 'Biology': 70, 'Data Structures': 95}, 's1081388': {'ROTC service': 95, 'Networks': 55, 'Accounting': 85, 'Community Service': 95, 'Calculus': 65}, 's1081139': {'Python': 80, 'Chemistry': 70, 'ROTC service': 50, 'Community Service': 60, 'History': 90}, 's1081341': {'Data Structures': 75, 'Algorithms': 85, 'English': 60, 'Networks': 55, 'Python': 45}, 's1081273': {'Economics': 70, 'Physics': 80, 'Biology': 80, 'Calculus': 95, 'Finance': 50}, 's1081194': {'Algorithms': 40, 'Data Structures': 90, 'Calculus': 55, 'History': 95, 'Networks': 40}, 's1081372': {'Biology': 50, 'Community Service': 90, 'Networks': 65, 'Calculus': 75, 'Physics': 75}, 's1081256': {'Biology': 50, 'History': 90, 'Data Structures': 95, 'Calculus': 95, 'Community Service': 70}, 's1081167': {'English': 60, 'Accounting': 75, 'History': 80, 'Finance': 60, 'Management': 40}, 's1081200': {'Chemistry': 65, 'Networks': 80, 'History': 70, 'Physics': 70, 'Algorithms': 50}, 's1081203': {'Chemistry': 40, 'Biology': 60, 'Calculus': 70, 'History': 40, 'Economics': 50}, 's1081237': {'Finance': 55, 'Community Service': 75, 'Algorithms': 45, 'Python': 55, 'Economics': 95}, 's1081259': {'Community Service': 90, 'Biology': 70, 'Management': 65, 'Finance': 55, 'Python': 70}, 's1081277': {'Networks': 95, 'Calculus': 65, 'Python': 75, 'Chemistry': 65, 'History': 50}, 's1081365': {'Physics': 80, 'Algorithms': 90, 'Finance': 40, 'English': 45, 'Calculus': 75}, 's1081324': {'Physics': 60, 'Economics': 65, 'Accounting': 45, 'Algorithms': 75, 'Networks': 80}, 's1081173': {'Management': 95, 'Accounting': 95, 'Networks': 75, 'ROTC service': 95, 'Chemistry': 55}, 's1081368': {'Accounting': 90, 'Finance': 75, 'Management': 45, 'English': 40, 'Algorithms': 60}, 's1081108': {'Networks': 40, 'Community Service': 45, 'Python': 95, 'Management': 85, 'Algorithms': 65}, 's1081120': {'English': 70, 'History': 70, 'Physics': 75, 'ROTC service': 75, 'Calculus': 85}}

# dicts of dicts

credits_dict = {'Accounting': 3, 'Algorithms': 3, 'Biology': 3, 'Calculus': 3, 'Chemistry': 3, 'Data Structures': 3, 'Economics': 3, 'English': 2, 'Finance': 3, 'History': 2, 'Management': 3, 'Networks': 3, 'Physics': 3, 'Python': 3}

# dicts
# 果先依 "平均高低遞減排序" ；若同分， 再依 "總學分數遞減排序" ；若學分數也相同，就依 "學號遞增排序。"
# s1081391': {'Finance': 65, 'Chemistry': 95, 'Economics': 65, 'English': 55, 'Accounting': 70}

avg_dict = {}  # item: (studentId, average)

# print("Student Scores and Average:")
# 將 grade_dict 的 結 果 迭 代 出 來
for key, value in grade_dict.items():
    # print(key, value) # optional, just to make sure I get correct data
    stu_sum = 0
    credits = 0
    f_credits = 0
    # grade_dict 中 抓 到的 value，做計算 sum 和 credits 的準備
    for c, s in value.items():
      stu_sum += s * credits_dict.setdefault(c, 0)
      credits += credits_dict.setdefault(c, 0)   # setdefault() 方法返回鍵的值 (如果鍵在字典中)。 如果沒有，它將在字典中插入帶有值的鍵。
      if s < 60:
          f_credits += credits_dict.setdefault(c, 0)  # setdefault() 方法返回鍵的值 (如果鍵在字典中)。 如果沒有，它將在字典中插入帶有值的鍵。

    average = stu_sum/credits # 計算和存入
    x = f_credits / credits
    failed_rated = x * credits

    avg_dict[key] = average, credits,failed_rated # store student's average to avg_dict

    # print("%s: %s, %.2f ,%.2f" % (key, value, average,failed_rated))


v_sorted_list = sorted(avg_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))
# sort avg_dict by average (DESC), then by credits (DESC)
# key=lambda x: (-x[1][0], -x[1][1]) 由大到小


print("\n----Top 5 performed students----")
for k, v in v_sorted_list[:6]:
    if v[1] >=  9:
        print("%s: %.2f, %2d credits" % (k, v[0], v[1]))


from collections import Counter

# # Create a counter object
counter = Counter(avg_dict)

# # 找到前五名掛科的人
top5f = counter.most_common()[:-6:-1]

print("\n----watch list ----")

for i in top5f:
    if i[1][2] >= 9 and i[1][2]/i[1][1] > 0.5:
        print("%s: Failed %2d out of %2d Credits" % (i[0], int(i[1][2]), i[1][1]))
    # i[1][0]中，陣列i[1]中的第零個
    # 當掉比率 = 當掉學分數/修課總學分數(已有)
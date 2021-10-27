import random

grade_dict = {'s1071122': {'Chemistry': 50, 'Networks': 80, 'Algorithms': 50, 'Community Service': 50, 'Accounting': 60, 'Physics': 50}, 's1071159': {'Management': 70, 'Finance': 70, 'Biology': 80, 'Physics': 50, 'Chemistry': 80, 'English': 80}, 's1071204': {'Finance': 70, 'Algorithms': 50, 'Chemistry': 50, 'Accounting': 80, 'Networks': 70, 'Management': 50}, 's1071281': {'Accounting': 90, 'English': 80, 'ROTC service': 80, 'Community Service': 70, 'Python': 60, 'Calculus': 90}, 's1071264': {'Biology': 80, 'Management': 80, 'Python': 50, 'History': 70, 'Economics': 90, 'Physics': 90}, 's1071161': {'Data Structures': 80, 'Finance': 50, 'Management': 80, 'Community Service': 80, 'Algorithms': 60, 'Chemistry': 80}, 's1071101': {'ROTC service': 50, 'History': 90, 'Management': 90, 'Chemistry': 60, 'Finance': 80, 'Algorithms': 60}, 's1071166': {'Chemistry': 90, 'ROTC service': 70, 'Economics': 90, 'Accounting': 60, 'Calculus': 50, 'Networks': 90}, 's1071382': {'Chemistry': 90, 'History': 50, 'Biology': 80, 'Physics': 60, 'Networks': 60, 'Management': 50}, 's1071387': {'Biology': 80, 'Community Service': 50, 'ROTC service': 50, 'Calculus': 90, 'Management': 50, 'Physics': 70}, 's1071352': {'Algorithms': 90, 'Chemistry': 90, 'Biology': 70, 'Calculus': 60, 'Management': 90, 'Finance': 90}, 's1071163': {'Biology': 60, 'Data Structures': 60, 'Economics': 70, 'Finance': 80, 'Algorithms': 70, 'Community Service': 50}, 's1071252': {'Networks': 80, 'Python': 60, 'ROTC service': 90, 'Calculus': 90, 'English': 50, 'Management': 60}, 's1071182': {'Economics': 50, 'Management': 70, 'Algorithms': 70, 'English': 70, 'Finance': 50, 'History': 70}, 's1071191': {'Networks': 80, 'Community Service': 90, 'Management': 80, 'Biology': 90, 'Data Structures': 70, 'ROTC service': 70}, 's1071370': {'Management': 70, 'Python': 90, 'Community Service': 80, 'Finance': 80, 'Chemistry': 90, 'Economics': 50}, 's1071203': {'Accounting': 70, 'Finance': 50, 'Networks': 70, 'Management': 70, 'Algorithms': 60, 'Calculus': 60}, 's1071377': {'Economics': 70, 'Community Service': 90, 'Chemistry': 70, 'Accounting': 80, 'Algorithms': 50, 'History': 70}, 's1071385': {'Physics': 90, 'English': 60, 'Accounting': 50, 'ROTC service': 80, 'Python': 70, 'Networks': 90}, 's1071174': {'Management': 70, 'Biology': 60, 'English': 90, 'Data Structures': 90, 'Community Service': 60, 'Finance': 50}, 's1071368': {'Networks': 80, 'Physics': 60, 'Community Service': 90, 'History': 90, 'Python': 90, 'Biology': 90}, 's1071351': {'Biology': 50, 'Calculus': 80, 'History': 50, 'Data Structures': 90, 'English': 70, 'Chemistry': 90}, 's1071289': {'Finance': 80, 'Economics': 80, 'Algorithms': 60, 'Accounting': 90, 'Biology': 70, 'ROTC service': 50}, 's1071210': {'Chemistry': 80, 'Physics': 70, 'Management': 50, 'ROTC service': 60, 'Python': 50, 'English': 80}, 's1071108': {'Calculus': 50, 'Physics': 90, 'Biology': 80, 'History': 50, 'Community Service': 60, 'Economics': 90}, 's1071333': {'Economics': 90, 'History': 60, 'Calculus': 90, 'Physics': 80, 'Networks': 70, 'Biology': 80}, 's1071257': {'Python': 90, 'Finance': 90, 'Community Service': 70, 'History': 60, 'Data Structures': 50, 'Accounting': 50}, 's1071336': {'Finance': 50, 'Physics': 50, 'Accounting': 90, 'Management': 50, 'Data Structures': 90, 'Community Service': 50}, 's1071193': {'Physics': 70, 'English': 80, 'Networks': 50, 'Community Service': 80, 'Management': 80, 'Calculus': 90}, 's1071181': {'Finance': 90, 'Community Service': 70, 'Calculus': 60, 'Physics': 60, 'Accounting': 70, 'Algorithms': 60}, 's1071225': {'ROTC service': 80, 'Python': 60, 'Calculus': 60, 'Economics': 90, 'Management': 90, 'Networks': 50}, 's1071383': {'Networks': 80, 'Economics': 80, 'Python': 80, 'Algorithms': 60, 'Community Service': 80, 'Management': 50}, 's1071228': {'Accounting': 90, 'Biology': 80, 'Physics': 80, 'Economics': 60, 'Networks': 50, 'Finance': 80}, 's1071285': {'Finance': 70, 'Chemistry': 60, 'Python': 80, 'Data Structures': 80, 'Algorithms': 50, 'Community Service': 80}, 's1071342': {'Physics': 80, 'Python': 90, 'Data Structures': 70, 'Algorithms': 60, 'Accounting': 50, 'Chemistry': 80}, 's1071154': {'Community Service': 80, 'Calculus': 50, 'Accounting': 90, 'Economics': 90, 'Finance': 50, 'Algorithms': 60}, 's1071110': {'Networks': 70, 'Python': 50, 'Physics': 90, 'Economics': 50, 'Biology': 90, 'Chemistry': 70}, 's1071227': {'Data Structures': 60, 'History': 50, 'Economics': 50, 'Chemistry': 50, 'Accounting': 90, 'Calculus': 70}, 's1071231': {'Finance': 90, 'Python': 90, 'Chemistry': 60, 'History': 60, 'Networks': 70, 'ROTC service': 80}, 's1071235': {'Calculus': 50, 'English': 80, 'Chemistry': 90, 'Accounting': 50, 'Management': 70, 'Physics': 60}, 's1071337': {'Biology': 50, 'Accounting': 70, 'Data Structures': 70, 'Finance': 60, 'Economics': 70, 'Calculus': 80}, 's1071132': {'Biology': 90, 'Algorithms': 60, 'Networks': 70, 'History': 70, 'ROTC service': 80, 'Python': 60}, 's1071111': {'Networks': 90, 'Calculus': 50, 'Economics': 90, 'Chemistry': 90, 'Python': 90, 'History': 50}, 's1071138': {'Biology': 80, 'Chemistry': 80, 'Finance': 60, 'Community Service': 90, 'Physics': 80, 'Networks': 50}, 's1071255': {'Community Service': 80, 'English': 60, 'Physics': 80, 'ROTC service': 70, 'Calculus': 60, 'History': 70}, 's1071327': {'Accounting': 90, 'Calculus': 50, 'History': 80, 'English': 90, 'Data Structures': 90, 'Management': 50}, 's1071126': {'Accounting': 60, 'Biology': 70, 'Calculus': 60, 'Algorithms': 80, 'Chemistry': 60, 'English': 80}, 's1071254': {'Data Structures': 70, 'Python': 80, 'History': 70, 'Biology': 90, 'Finance': 90, 'Networks': 90}, 's1071274': {'English': 50, 'Networks': 60, 'Algorithms': 60, 'Economics': 70, 'Management': 80, 'Physics': 50}, 's1071219': {'Algorithms': 50, 'ROTC service': 60, 'Management': 90, 'History': 60, 'Physics': 90, 'Economics': 50}, 's1071146': {'Networks': 60, 'Biology': 50, 'Physics': 80, 'Finance': 60, 'Data Structures': 90, 'Economics': 80}, 's1071330': {'Community Service': 80, 'Physics': 60, 'Networks': 80, 'Biology': 90, 'ROTC service': 60, 'Data Structures': 90}, 's1071118': {'Biology': 80, 'Calculus': 60, 'Finance': 60, 'Community Service': 60, 'Data Structures': 60, 'English': 90}, 's1071201': {'Finance': 70, 'English': 60, 'Networks': 70, 'Python': 90, 'Chemistry': 80, 'Physics': 70}, 's1071363': {'History': 80, 'Algorithms': 70, 'Finance': 60, 'ROTC service': 50, 'Calculus': 60, 'Physics': 90}, 's1071293': {'English': 80, 'Physics': 80, 'History': 80, 'Data Structures': 50, 'Accounting': 50, 'Finance': 90}, 's1071346': {'Networks': 90, 'Calculus': 70, 'English': 80, 'Economics': 80, 'Accounting': 60, 'Finance': 80}, 's1071129': {'Python': 80, 'Calculus': 90, 'ROTC service': 90, 'Biology': 80, 'Networks': 70, 'Accounting': 70}, 's1071175': {'Community Service': 90, 'Economics': 70, 'Biology': 60, 'History': 60, 'ROTC service': 80, 'Management': 90}, 's1071192': {'Finance': 80, 'English': 60, 'Management': 60, 'ROTC service': 90, 'Chemistry': 60, 'Physics': 70}}
# dictt of dicts

credits_dict = {'Finance': 3, 'Calculus':3, 'English':2, 'Biology':3, 'Economics':3, "Accounting":3, 'Python':3, 'Management':3, 'Networks':3, 'Algorithms':3, 'Data Structures':3, 'Physics':3, 'Chemistry':3, 'History':2}
# dicts
# 果先依 "平均高低遞減排序" ；若同分， 再依 "總學分數遞減排序" ；若學分數也相同，就依 "學號遞增排序。"

# s1071192: {'Finance': 80, 'English': 60, 'Management': 60, 'ROTC service': 90, 'Chemistry': 60, 'Physics': 70}, 66.43

avg_dict = {} # item: (studentId, average)

print("Student Scores and Average:")

# 將 grade_dict 的 結 果 迭 代 出 來
for key, value in grade_dict.items():
    # print(key, value) # optional, just to make sure I get correct data
    stu_sum = 0
    credits = 0

    # grade_dict 中 抓 到的 value，做計算 sum 和 credits 的準備
    for c, s in value.items():
      stu_sum += s * credits_dict.setdefault(c, 0)
      credits += credits_dict.setdefault(c, 0)   # setdefault() 方法返回鍵的值 (如果鍵在字典中)。 如果沒有，它將在字典中插入帶有值的鍵。

    average = stu_sum/credits # 計算和存入
    avg_dict[key] = average, credits # store student's average to avg_dict
    print("%s: %s, %.2f " % (key, value, average))

v_sorted_list = sorted(avg_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))
# sort avg_dict by average (DESC), then by credits (DESC)
# key=lambda x: (-x[1][0], -x[1][1]) 由大到小



print("\nTop 10 performed students")
for k, v in v_sorted_list[:10]:
    print("%s: %.2f, %2d Credits"  % (k, v[0], v[1]))
    


# # Finding the top five
from collections import Counter

# # Create a counter object
counter = Counter(avg_dict)
  
# # Finding 5 highest values 
top5s = counter.most_common(5)
  
print("\nDict with 5 highest values:")
  
for i in top5s:
  print("%s: %.2f, %2d Credits" % (i[0], i[1][0], i[1][1]))
  # i[1][0]中，陣列i[1]中的第零個
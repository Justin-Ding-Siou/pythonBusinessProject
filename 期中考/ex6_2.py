# 樂透包牌: 從 10個數字 4, 6, 7, 8, 11, 24, 35, 37, 40, 48 取6個數字。
# 找出所有的組合 （共 210組），並顯示數字組合最大的最後5個組合。

# 例如：
# 206: (8, 11, 24, 35, 40, 48)
# 207: (8, 11, 24, 37, 40, 48)
# 208: (8, 11, 35, 37, 40, 48)
# 09: (8, 24, 35, 37, 40, 48)
# 210: (11, 24, 35, 37, 40, 48)

import random
rand_List = [4, 6, 7, 8, 11, 24, 35, 37, 40, 48]

from itertools import combinations, permutations

# 找到所有的組合
value_list = list(combinations([4, 6, 7, 8, 11, 24, 35, 37, 40, 48], 6))
# print(value_list)
for i in value_list:
    value_list_sum = sum(i)
    # print(value_list_sum)
    # 為每個 list 進行總和加總




# 顯示編號
# List Comprehensions
key_list = [i for i in range(1,211)]
# print(key_list)

# 兩列表組合
dict_form_list = dict(zip(key_list, value_list))
# print(dict_form_list)



# 找到前5個最大值

for i in range(206,211):
    max_5_list = dict_form_list[i]
    print(i,":",max_5_list)



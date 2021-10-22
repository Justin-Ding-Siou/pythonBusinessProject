import random

# 一組樂透號碼產生器
def lotto(n, m): # 從[1..n] 選m個號碼, 不重覆
    lst = list()
    nums = [i for i in range(1, n+1)]
    for i in range(m):
        n = random.choice(nums)
        lst.append(n)
        nums.remove(n)
    # alternative
    lst = random.sample(nums, m)
    lst = [str(n).zfill(2) for n in lst]
    return lst

lotto_lst = []
i = 0
while (i < 7):
    picks = sorted(lotto(49, 6))
    if picks in lotto_lst:
        continue
    else:
        lotto_lst.append(picks)
        i = i + 1

# print(*lotto_lst)
for e in lotto_lst:
    print(e)
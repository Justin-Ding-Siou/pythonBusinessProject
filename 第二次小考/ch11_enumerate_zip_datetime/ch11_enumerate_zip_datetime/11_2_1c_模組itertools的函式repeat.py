import itertools

nums = [1, 2, 3]

# itertools.repeat(object[, times]): 使用object 重複 times 產生資料列
repeatnums = itertools.repeat(nums, 3)

for i in range(3):
    nums = repeatnums.__next__()
    print(nums)


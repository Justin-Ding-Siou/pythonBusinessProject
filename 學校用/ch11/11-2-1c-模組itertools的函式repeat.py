import itertools
nums = [1, 2, 3]
repeatnums = itertools.repeat(nums, 3)
for i in range(3):
    num = repeatnums.__next__()
    print(num)


import itertools
nums = [i for i in range(1, 6)]
sums = itertools.accumulate(nums)
print(list(sums))
sums = itertools.accumulate(nums, lambda x,y:x*y)
print(list(sums))
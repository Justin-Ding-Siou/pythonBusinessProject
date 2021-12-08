import itertools

nums = [i for i in range(1, 6)]
print(nums)

# itertools.accumulate(iterable[, func]): 對 iterable 物件執行func後累加
sums = itertools.accumulate(nums)
print(list(sums))

sums = itertools.accumulate(nums, lambda x, y: x*y)
print(list(sums))
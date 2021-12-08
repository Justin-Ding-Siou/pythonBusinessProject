import itertools

nums = [1, 2, 3]
# itertools.cycle(iterable): 使用iterable 循環產生資料列
cyclenums = itertools.cycle(nums)

for i in range(6):
    num = cyclenums.__next__()
    print(num)
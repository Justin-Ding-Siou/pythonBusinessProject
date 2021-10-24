import itertools
nums = [1, 2, 3]
cyclenums = itertools.cycle(nums)
for i in range(6):
    num = cyclenums.__next__()
    print(num)
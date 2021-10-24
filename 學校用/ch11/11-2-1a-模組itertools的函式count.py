import itertools
nums = itertools.count(1,2)
for i in range(5):
    num = nums.__next__()
    print(num)
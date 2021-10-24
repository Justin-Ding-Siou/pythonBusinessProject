import functools
num = functools.reduce(lambda x, y:x+y, range(1,10))
print(num)
num = functools.reduce(lambda x, y:x+y, range(1,10),3)
print(num)
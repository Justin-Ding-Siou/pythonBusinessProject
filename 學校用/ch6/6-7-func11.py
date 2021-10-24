def irange(start, stop, step=1):
    if start < stop:
        i = start
        while i < stop:
            yield i
            i = i + step
    else:
        i = start
        while i > stop:
            yield i
            i = i + step
x = irange(1,10)
print(x)
for i in irange(1, 5, 1):
    print(i)
for i in irange(4, 1, -1):
    print(i)
import functools

# reduce(function, sequence[,initial]): continually applies the function to the sequence.
# It returns a single value.

# 從 1 加到 9, 初始總和值 0 
num = functools.reduce(lambda x, y: x+y, range(1,10))
print(num)

# 從 1 加到 9, 初始總和值 3 
num = functools.reduce(lambda x, y: x+y, range(1,10), 3)
print(num)
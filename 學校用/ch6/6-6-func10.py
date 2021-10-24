def run(func, x, y):
    return func(x, y)
k = run(lambda a,b: a+b, 10, 20)
print('k=', k)
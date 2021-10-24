def add(a, b):
    return a + b
def run(func, x, y):
    return func(x, y)
k = run(add, 10, 20)
print('k=', k)
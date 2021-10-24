from collections import Counter
c = Counter('Python')
print(c)
x = ['a', 'a', 'b', 'b', 'b']
c = Counter(x)
print(c)
c = Counter({'a':2,'b':3})
print(c)
c = Counter(a=2, b=3)
print(c)
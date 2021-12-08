from collections import Counter
c = Counter({'a':2,'b':3,'c':1})
print(c)
print(list(c.elements()))
print(c.values())
print(c.keys())

# c.most_common([n]): 找出最常出現的n個元素，預設全部
print(c.most_common())
print(c.most_common(1))
print(c.most_common()[::-1])
print(c.most_common()[:-2:-1]) # [-1:-2:-1]
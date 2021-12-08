from collections import Counter

c1 = Counter(a=2, b=3)
c2 = Counter(b=2, c=1)

print("c1 =", c1)
print("c2 =", c2)
print()

# c1 + c2: c1 與 c2 相同元素的次數相加
print(c1 + c2)
print()

# c1 - c2: c1 與 c2 相同元素的次數差異
print(c1 - c2)
print()

# c1 & c2: c1 與 c2 相同元素的次數取少者 (and)
print(c1 & c2)
print()

# c1 | c2: c1 與 c2 相同元素的次數取多者 (or)
print(c1 | c2)
from collections import Counter
import re

fin = open('zen.txt', 'rt')
s = fin.read().lower()

# 找出字母，數字，底線組合的字串，越長越好
words = re.findall(r"[\w]+", s)
#words = re.findall(r"[\w]+'[\w]+|[\w]+'|[\w]+", s)

c = Counter(words)
print(c.most_common(5))
print(c)

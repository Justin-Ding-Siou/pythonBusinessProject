from collections import Counter
import re
fin = open('zen.txt', 'rt')
s = fin.read().lower()
words = re.findall(r'[\w\']+',s)
c = Counter(words)
print(c.most_common(5))

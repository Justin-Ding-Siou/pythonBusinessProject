# -*- coding: utf-8 -*-
"""
Find top 3 items

"""
from collections import Counter
from heapq import nlargest

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(my_dict)
print()

# dict.get() returns the value for the given key, if present in the dictionary. 
# otherwise, it will return None

# 1: Using sorted
sorted1 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
sorted2 = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
sorted3 = sorted(my_dict, key=my_dict.get, reverse=True)
print("Top 3 keys:", sorted3[0:3])

# 2: Using heapq.nlargest
three_largest = nlargest(3, my_dict, key=my_dict.get)
print("Top 3 keys:", three_largest) 

# 3: Using collections.Counter()
counter = Counter(my_dict)
highs = counter.most_common(3)
print("Top 3 keys:", [x[0] for x in highs])

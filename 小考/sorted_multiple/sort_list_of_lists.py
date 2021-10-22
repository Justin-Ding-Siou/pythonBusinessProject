# Sorting on list of lists (or tuples, dicts)

from operator import itemgetter

lst = [['sarah', 'Jr', 30], ['jack', 'So', 20], ['rich', 'So', 20], ['bill', 'Jr', 20]]

# default: sort by item[0]
print("sort1:", sorted(lst))
print()

# sort by item[1]
print("sort2:", sorted(lst, key=itemgetter(1)))
print("sort2:", sorted(lst, key=lambda e: e[1]))
print()

# sort by item[2]
print("sort3:", sorted(lst, key=itemgetter(2)))
print("sort3:", sorted(lst, key=lambda e: e[2]))
print()

# sort by item[1] first, then by item[2]
print("sort4:", sorted(lst, key=itemgetter(1, 2)))
print("sort4:", sorted(lst, key=lambda e: (e[1], e[2])))
print()

# sort by item[1] first, then by item[2], reverse
print("sort5:", sorted(lst, key=itemgetter(1, -2)))
print("sort5:", sorted(lst, key=lambda e: (e[1], -e[2])))
print()

# sort by item[1] first, then by item[2], reverse, 
# and finally item[0] 
print("sort6:", sorted(lst, key=itemgetter(1, -2, 0))) # seems wrong
print("sort6:", sorted(lst, key=lambda e: (e[1], -e[2], e[0])))
print()

# sort by item[1] first, then by item[2] (reverse), 
# and finally item[0] (reverse)

# Last key goes first in multiple passes
lst1 = lst.copy()
lst1.sort(key=lambda e: e[0], reverse=True)
lst1.sort(key=lambda e: (e[1], -e[2]))
print("sort7:", lst1)

# For a completely generic option:
data = lst.copy()
keys = [ (1, False), (2, True), (0, True) ]
for key, rev in reversed(keys):
    data.sort(key=itemgetter(key), reverse=rev)
print("sort7:", data)
print()


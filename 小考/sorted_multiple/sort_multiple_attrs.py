# Sorted  multiple attributes

# Case 1
# Sort by item[1] (DESC), then item[0] (ASC) - one pass
lst = [('B', 3), ('A', 1), ('A', 2), ('I', 1), ('J', 1)]
lst1 =sorted(lst, key=lambda x:(-x[1], x[0]))
print("Sort by reverse item[1], then by item[0]:", lst1)
print()

# Sort by multiple passes
lst1 = lst.copy()

## sort by item[0] (secondary)
lst1.sort(key=lambda x: x[0])

## sort by reverse item[1] (primary)
lst1.sort(key=lambda x: x[1], reverse=True)

print("Sort by reverse item[1], then by item[0]:", lst1)
print()

from operator import itemgetter
lst1 = lst.copy()
lst1.sort(key=itemgetter(0))
# print("lst sorted by item[0]:", lst1)
lst1.sort(key=itemgetter(1),reverse=True)
print("Sort by reverse item[1], then by item[0]:", lst1)
print()

lst2 = sorted(lst, key=itemgetter(-1, 0))
print("Sort by reverse item[1], then by item[0]:", lst2)
print("Itemgetter seems wrong\n")

# Case2
DATA = [
    ('Jones', 'Jane', 58),
    ('Smith', 'Anne', 30),
    ('Jones', 'Fred', 30),
    ('Smith', 'John', 60),
    ('Smith', 'Fred', 30),
    ('Jones', 'Anne', 30),
    ('Smith', 'Jane', 58),
    ('Smith', 'Twin2', 3),
    ('Jones', 'John', 60),
    ('Smith', 'Twin1', 3),
    ('Jones', 'Twin2', 3),
    ('Jones', 'Twin3', 3)
]

# Sort by Surname, Age DESC, Firstname
print("\nInitial data")
for d in DATA:
    print("{:10s} {:10s} {}".format(*d))

print()
# Sort by Surname, Age DESC, Firstname
print("Sort by Surname, Age DESC, Firstname")
print('Sorted results1： Primary key comes first.')
lst1 = sorted(DATA, key=lambda row: (row[0], -row[2], row[1]))
for d in lst1:
    print("{:10s} {:10s} {}".format(*d))

# print('\nSorted results2: Seems wrong')
# lst2 = sorted(DATA, key=itemgetter(0, -2, 1))
# for d in lst2:
    # print("{:10s} {:10s} {}".format(*d))

# For a completely generic option:
print('\nSorted results3 - completely generic option')
data = DATA.copy()
keys = [ (0, False), (2, True), (1, True) ]
for key, rev in reversed(keys):
    data.sort(key=itemgetter(key), reverse=rev)
for d in data:
    print("{:10s} {:10s} {}".format(*d))

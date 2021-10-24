import itertools
perm = itertools.permutations('ABC', 2)
print(list(perm))
comb = itertools.combinations('ABC', 2)
print(list(comb))
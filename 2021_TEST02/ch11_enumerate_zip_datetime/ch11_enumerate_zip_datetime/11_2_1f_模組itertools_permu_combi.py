import itertools

# itertools.permutations(iterable[, r]): 對 iterable 物件取r個元素的所有排列
perm = itertools.permutations('ABC', 2)
print(list(perm))

# itertools.combinations(iterable[, r]): 對 iterable 物件取r個元素的所有組合
comb = itertools.combinations('ABC', 2)
print(list(comb))
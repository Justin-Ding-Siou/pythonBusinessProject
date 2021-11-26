import itertools

# itertools.chain(*iterable): 對多個iterable 物件取出所有元素，串接成新數列
s = itertools.chain('Py','thon')
print(list(s))
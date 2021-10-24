import pprint
print('在函式外，顯示全域變數', globals())
print('在函式外，顯示區域變數', locals())
def add(x, y):
    sum = x+y
    print('在函式內，顯示全域變數')
    pprint.pprint(globals())
    print('在函式內，顯示區域變數')
    pprint.pprint(locals())
    return sum
ans = add(1,2)

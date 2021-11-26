import pprint

print('\n在函式外，顯示全域變數', globals())
print('\n在函式外，顯示區域變數', locals())

def add(x, y):
    sum = x+y
    print('\n在函式內，顯示全域變數')
    pprint.pprint(globals())
    print('\n在函式內，顯示區域變數')
    pprint.pprint(locals())
    return sum

ans = add(1,2)

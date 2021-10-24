w = float(input('請輸入物品重量？'))
if w <= 5:
    print('所需郵資為50元')
elif w <= 10:
    print('所需郵資為70元')
elif w <= 15:
    print('所需郵資為90元')
elif w <= 20:
    print('所需郵資為110元')
else:
    print('超過20公斤無法寄送')


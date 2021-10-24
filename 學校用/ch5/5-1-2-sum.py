s = int(input('請輸入加總開始值？'))
e = int(input('請輸入加總終止值？'))
inc = int(input('請輸入遞增減值？'))
sum = 0
for i in range(s, e, inc):
    sum = sum + i
    print('i為', i, '加總結果為', sum)
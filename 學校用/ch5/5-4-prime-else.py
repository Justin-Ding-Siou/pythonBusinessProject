import math
num = int(input('請輸入一個整數？'))
j = 2
while j < math.sqrt(num):
    if (num%j == 0):
        print(num, '不是質數')
        break
    j += 1
else:
    print(num, '是質數')

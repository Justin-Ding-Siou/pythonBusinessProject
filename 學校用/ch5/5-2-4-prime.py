num = int(input('請輸入一個整數？'))
j = 2
prime = True
while j < num:
    if (num%j == 0):
        prime = False
        break
    j += 1
if prime:
    print(num, '是質數')
else:
    print(num, '不是質數')
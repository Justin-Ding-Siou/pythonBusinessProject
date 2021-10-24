num = int(input('輸入求第幾項費氏數列？'))
a = 1
b = 1
print(1,a)
for i in range(2, num+1):
    a, b = b, a+b
    print(i, a)
M = int(input('請輸入M？'))
fac = 1
i = 1
while(fac < M):
    i = i + 1
    fac = fac * i
print(i,'階乘為', fac,'大於', M)
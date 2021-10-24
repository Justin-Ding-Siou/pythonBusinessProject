def fac(num):
    if num == 1:
        return 1
    else:
        return num*fac(num-1)
n = int(input('請輸入n值？'))
ans = fac(n)
print(n,'!為',ans,sep='')

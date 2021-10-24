def gcd(m, n):
    if m == 0:
        return n
    else:
        print(m, '與', n, '的最大公因數相當於', n % m, '與', m, '的最大公因數', sep='')
        return gcd(n % m, m)
m = int(input('請輸入m值？'))
n = int(input('請輸入n值？'))
ans = gcd(m, n)
print(m, '與', n, '的最大公因數為', ans, sep='')

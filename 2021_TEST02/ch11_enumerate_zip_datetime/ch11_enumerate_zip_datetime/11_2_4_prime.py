import itertools

def iter_primes(): # a generator function
     numbers = itertools.count(2)
     while True:
         prime = numbers.__next__()
         print("prime:", prime)
         # Implements reflected modulo using the % operator.
         # x % y ==	y.__rmod__(x)
         # 留下除不盡 prime 的number
         numbers = filter(prime.__rmod__, numbers)
         # print("numbers:", numbers)
         yield prime

# 找尋 1000 以內的質數
for p in iter_primes():
    if p > 1000:
        break
    print(p, ' ', end='')
print()
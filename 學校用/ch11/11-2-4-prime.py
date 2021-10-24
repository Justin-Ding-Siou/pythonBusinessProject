import itertools
def iter_primes():
     numbers = itertools.count(2)
     while True:
         prime = numbers.__next__()
         numbers = filter(prime.__rmod__, numbers)
         yield prime
for p in iter_primes():
    if p > 1000:
        break
    print(p,' ',end='')

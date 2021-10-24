import math
for i in range(2,1000):
    j = 2
    prime = True
    while j <= math.sqrt(i):
        if (i%j == 0):
            prime = False
            break
        j += 1
    if prime:
        print(i,'為質數')
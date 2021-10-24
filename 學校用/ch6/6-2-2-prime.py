import math
def prime(num):
    j = 2
    while j <= math.sqrt(num):
        if (num%j == 0):
            return False
        j += 1
    return True
for i in range(2, 101):
    if prime(i):
        print(i, '為質數')
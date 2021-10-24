import random
def lotto(n, m):
    prize = list()
    nums = [i for i in range(1, n+1)]
    for i in range(m):
        n = random.choice(nums)
        prize.append(n)
        nums.remove(n)
    return prize

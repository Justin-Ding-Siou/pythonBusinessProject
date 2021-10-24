import random
def reciept():
    prize = ''
    nums = [i for i in range(10)]
    for i in range(8):
        n = random.choice(nums)
        prize += str(n)
    return prize

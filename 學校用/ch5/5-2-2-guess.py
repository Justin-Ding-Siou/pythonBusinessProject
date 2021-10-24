import random
target = random.randint(1,99)
guess = 0
while target != guess:
    guess = int(input('請輸入1到99的數字？'))
    if target < guess:
        print('猜小一點')
    elif target > guess:
        print('猜大一點')
    else:
        print('猜中了')
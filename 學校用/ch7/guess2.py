from guess import figure_guess
def run():
    computer = figure_guess()
    my = input('請輸入「剪刀」、「石頭」或「布」？')
    print('電腦出', computer)
    if my == '剪刀':
        if computer == '剪刀':
            print('平手')
        elif computer == '石頭':
            print('電腦獲勝')
        else:
            print('玩家獲勝')
    elif my == '石頭':
        if computer == '剪刀':
            print('玩家獲勝')
        elif computer == '石頭':
            print('平手')
        else:
            print('電腦獲勝')
    else:
        if computer == '剪刀':
            print('電腦獲勝')
        elif computer == '石頭':
            print('玩家獲勝')
        else:
            print('平手')
if __name__ == '__main__':
    for i in range(10):
        run()
else:
    print('我不是獨立執行的python程式')
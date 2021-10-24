try:
    pwd = input('請輸入密碼')
except EOFError:
    print('輸入EOF')
else:
    print('輸入密碼為', pwd)
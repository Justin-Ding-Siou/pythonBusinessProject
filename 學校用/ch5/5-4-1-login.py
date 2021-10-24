while True:
    acc = input('請輸入帳號？')
    pwd = input('請輸入密碼？')
    if (acc == 'abc' and pwd == '123'):
        print('帳號與密碼正確')
        break
    else:
        print('登入失敗')
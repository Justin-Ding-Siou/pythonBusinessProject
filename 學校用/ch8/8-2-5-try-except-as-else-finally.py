class PwdException(Exception):
    def __init__(self,pwd,len):
        super().__init__(self)
        self.pwd=pwd
        self.len=len
try:
    pwd = input('請輸入密碼，長度至少8個字元')
    if len(pwd) < 8:
        raise PwdException(pwd,len(pwd))
except EOFError:
    print('輸入EOF')
except PwdException as pex:
    print('密碼', pex.pwd, '長度為', pex.len, '密碼長度不足')
else:
    print('輸入密碼為', pwd)
finally:
    print('請妥善保管密碼')
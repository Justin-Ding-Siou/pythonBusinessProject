def debug(func1):
    def func2(*args, **kwargs):
        print('正在執行函式', func1.__name__)
        print('函式的說明文件為', func1.__doc__)
        print('位置引數', args)
        print('關鍵引數', kwargs)
        return func1(*args, **kwargs)
    return func2
def add(a, b):
    '回傳a加b的結果'
    return a+b
add = debug(add)
print(add(1, b=2))
@debug
def add(a, b, c):
    '回傳a+b+c的結果'
    return a+b+c
print(add(1, 2, c=3))
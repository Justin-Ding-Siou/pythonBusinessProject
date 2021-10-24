def func1(*args):
    print('位置引數為', args)
func1(1, 2, 3)
def func2(**kwargs):
    print('關鍵字引數為', kwargs)
func2(a=1, b=2)
def func3(start, *args, **kwargs):
    print("start=", start)
    print("位置引數為", args)
    print("關鍵字引數為", kwargs)
func3(1, 2, 3, a=4, b=5)

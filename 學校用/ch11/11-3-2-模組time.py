import time
now = time.time()
print(now)
print(time.ctime())
t=time.localtime()
print(t)
fmt = "%Y-%m-%d(%a) %H %M %S"
print('現在時間為',time.strftime(fmt))
fmt2 = "%Y-%B-%d(%A) %p %I %M %S"
print('現在時間為',time.strftime(fmt2))
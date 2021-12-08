import time

# time() function returns the number of seconds passed since
# January 1, 1970, 00:00:00
now = time.time()
print(now)

print(time.ctime()) # seconds to a string of local time

t = time.localtime() # time.struct_time
print(t)
print()

fmt = "%a, %Y-%m-%d %H:%M:%S"
print('現在時間為:', time.strftime(fmt))

fmt2 = "%Y-%B-%d (%A) %p %I:%M:%S"
print('現在時間為:', time.strftime(fmt2))
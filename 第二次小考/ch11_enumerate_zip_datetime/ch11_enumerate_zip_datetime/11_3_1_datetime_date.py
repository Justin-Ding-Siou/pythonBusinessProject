from datetime import datetime, date

now = date.today()
print(now)
print()

now = datetime.now()
print("Output 1:", now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second, now.microsecond)
print()

# datetime to string using strftime(): https://strftime.org/
print("Output 2:", now.strftime('%Y-%m-%d %H:%M:%S')) # 2020-09-19 20:09:55
print()

d = now.strftime("%d %b, %Y") # e.g., 19 Sep, 2020
print("Output 3:", d)
print()

d = now.strftime("%d %B, %Y") # e.g., 19 September, 2020
print("Output 4:", d)
print()

d = now.strftime("%I%p")    # 8PM
print("Output 5:", d)
print()






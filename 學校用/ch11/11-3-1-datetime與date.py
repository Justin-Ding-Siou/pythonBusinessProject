from datetime import datetime, date
now = date.today()
print(now)
now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second, now.microsecond)



from datetime import datetime,timedelta
birthday = datetime(1995,1,1,21,30,0,0)
print(birthday)
day10000 = timedelta(days=10000)
someday = birthday + day10000
print(someday)
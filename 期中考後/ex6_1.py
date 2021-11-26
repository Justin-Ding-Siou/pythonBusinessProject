from datetime import datetime,timedelta
birthday = datetime(1995,1,1,21,30,0,0)
print(birthday)
day10000 = timedelta(days=10000)
someday = birthday + day10000
print(someday)

# 找到今日的日期
# 增加天數
import datetime
today = datetime.date.today()
# 今日天氣
print(today)
# 下星期日立
for i in range(7,14):
    nextweek = today + datetime.timedelta(days=i)
    print(nextweek)



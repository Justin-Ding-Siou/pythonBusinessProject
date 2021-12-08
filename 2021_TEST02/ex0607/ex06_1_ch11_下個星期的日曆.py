from datetime import datetime,timedelta

now = datetime.now()
dw = 7 - now.weekday()    # days to next week
# dw = 7 - now.isoweekday() # days to next week

for i in range(0+dw, 7+dw):
    delta = timedelta(days=i)
    nextday = now + delta
    fmt = "%Y-%m-%d (%a)"
    print(nextday.strftime(fmt))
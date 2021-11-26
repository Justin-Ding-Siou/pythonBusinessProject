from datetime import datetime, timedelta

birthday = datetime(2021,1,1,21,30,0,0)
print(birthday)

day365 = timedelta(days=365)
someday = birthday + day365

month_one = timedelta(days=31) # 一個月是 28, 29, 30 還是 31 天？
someday2 = birthday - month_one

print("One year later:", someday)
print("One month ago: ", someday2)
print()

# Use dateutil.relativedelta for exact month's days
from datetime import date
from dateutil.relativedelta import relativedelta

one_month_ago = date.today() + relativedelta(months=-1)
six_months_later = date.today() + relativedelta(months=+6)
print("one_month_ago from today:   ", one_month_ago)
print("six_months_later from today:", six_months_later)

# one_month_ago 另解
d = date.today()
one_month_ago = (d.replace(day=1) - timedelta(days=1)).replace(day=d.day)
print(one_month_ago)
six_month_later = (d + timedelta(days=180)).replace(day=d.day)
print(six_months_later)

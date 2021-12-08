import collections

days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
sport = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球']
week_act = zip(days, sport)
d1 = dict(week_act)
print(d1)

week_act = zip(days, sport)
d2 = collections.OrderedDict(week_act)
print(d2)

od3 = collections.OrderedDict([('Cr', 1),('To', 2)])
print(od3)
d3 = dict([('Cr', 1),('To', 2)])
print(d3)

# OrderDict vs dict
# As of Python 3.7, the insertion-order preservation nature of dict objects 
# has been an official part of the Python language spec.

# Minor differences
# they are equal with content and order
assert d3 == od3
assert list(d3.items()) == list(od3.items())
assert repr(dict(od3)) == repr(d3)  # unambiguous
# assert str(od3) == str(d3)          # readable

import datetime
today = datetime.datetime.now()
  
# Print readable format for date-time object
print (str(today))
  
# print the official format of date-time object
print (repr(today)) 

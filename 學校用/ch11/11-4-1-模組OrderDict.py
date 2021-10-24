import collections
days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
sport = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球']
week = zip(days, sport)
d1 = dict(week)
print(d1)
week = zip(days, sport)
d2 = collections.OrderedDict(week)
print(d2)
d = collections.OrderedDict([('Cr', 1),('To', 2)])
print(d)
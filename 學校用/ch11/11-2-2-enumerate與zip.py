days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
p = enumerate(days, start=1)
for c, day in p:
    print(c, day)
do = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球', '壘球']
week = zip(days, do)
for day,sport in week:
    print(day,sport)

days = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']

# enumerate(iterable[, start]): 將iterable 元素從start依序編號，組成 (編號, 元素)
p = enumerate(days, start=1)
for c, day in p:
    print(c, day)

do = ['休息', '游泳','跑步', '籃球', '桌球', '羽球', '棒球', '壘球']

# zip(*iterable): 從每個iterable依序取出各一個元素，組成tuple
week_act = zip(days, do)

for day, sport in week_act:
    print(day, sport)

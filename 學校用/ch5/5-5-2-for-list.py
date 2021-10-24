sh = ['牛奶', '蛋', '咖啡豆']
for i in range(0,len(sh)):
    print (i, sh[i])
for i, name in enumerate(sh, start=1):
    print(i, name)
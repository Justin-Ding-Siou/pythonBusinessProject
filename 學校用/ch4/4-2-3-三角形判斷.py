a = int(input('請輸入三角形邊長a長度為？'))
b = int(input('請輸入三角形邊長b長度為？'))
c = int(input('請輸入三角形邊長c長度為？'))
if (a<b+c)and(b<a+c)and(c<a+b):
    print('可構成三角形')
else:
    print('無法構成三角形')

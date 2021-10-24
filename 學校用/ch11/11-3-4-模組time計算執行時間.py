import time as t
def count():
    st = t.time()
    [x for x in range(10000000)]
    et = t.time()
    print ('執行所需時間為',et-st,'秒')
count()

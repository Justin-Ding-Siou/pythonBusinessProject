import time as t

def count_time():
    st = t.time()
    # 放執行的程式區塊
    [x for x in range(100000000)]
    et = t.time()
    print ('\n執行所需時間為', round(et-st, 4),'秒\n')

count_time()

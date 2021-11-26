import itertools

# itertools.count(start[, step]): 從start開始產生無窮數列， 間隔step(預設 1)
nums = itertools.count(1, 2)

for i in range(5):
    num = nums.__next__() # nums的下一個元素
    print(num)
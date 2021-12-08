# map(function, sequence): apply function to every element of sequence
# returns an iterator

nums = [i for i in range(1, 6)]

def double(x):
    return 2*x

# 把每個元素加倍
nums2 = map(double, nums)
print(list(nums2))

# 從a,b 各取一個個元素來相乘
a = [i for i in range(1, 6)]  # 1, 2, 3, 4, 5
b = [i for i in range(6, 11)] # 6, 7, 8, 9, 10
c = map(lambda x, y: x*y, a, b)
print(list(c))
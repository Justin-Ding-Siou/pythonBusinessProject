nums = [i for i in range(1,6)]
def double(x):
    return 2*x
nums2 = map(double, nums)
print(list(nums2))
a = [i for i in range(1,6)]
b = [i for i in range(6,11)]
c = map(lambda x,y:x*y, a, b)
print(list(c))
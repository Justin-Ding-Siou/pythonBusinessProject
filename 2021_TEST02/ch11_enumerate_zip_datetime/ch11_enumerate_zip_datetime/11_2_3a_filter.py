# filter(function, sequence)： 
# 過濾sequence，留下function returns True 的元素

nums = [i for i in range(1,10)]

# 用 filter 找奇數
nums1 = filter(lambda x: x%2, nums)
print(nums1)       # a filter object
print(list(nums1)) # Convert filter object into list

# 用 filter 找偶數
nums2 = filter(lambda x: x%2 == 0, nums)
print(list(nums2))

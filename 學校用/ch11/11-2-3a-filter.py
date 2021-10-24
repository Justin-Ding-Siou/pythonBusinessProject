nums = [i for i in range(1,10)]
nums2 = filter(lambda x:x%2, nums)
print(list(nums2))
nums2 = filter(lambda x:x%2 == 0, nums)
print(list(nums2))

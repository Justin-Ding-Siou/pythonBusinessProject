import itertools

nums = [4, 6, 7, 8, 11, 24, 35, 37, 40, 48]
comb = list(itertools.combinations(nums, 6))
# print(len(comb))

for count, data in enumerate(list(comb)[-5:],start=len(comb)-5):
    print(f"{count+1}: {data}")

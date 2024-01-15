def twoSum(nums, target):
    prevDiff = {}

    for ind, ele in enumerate(nums):
        if ele in prevDiff:
            return [ind, prevDiff[ele]]
        prevDiff[target - ele] = ind
print(twoSum([2,7,11,15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))


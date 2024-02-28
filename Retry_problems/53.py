def maximum_subarray(nums):
    result = nums[0]
    Sum = 0

    for i in range(len(nums)):
        Sum += nums[i]

        if Sum > result:
            result = Sum
        if Sum < 0:
            Sum = 0

    return result
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [1]
nums2 = [5, 4, -1, 7, 8]
nums3 = [-1, 2, -5]
nums4 = [-1, 8]

print(maximum_subarray(nums))
print(maximum_subarray(nums1))
print(maximum_subarray(nums2))
print(maximum_subarray(nums3))
print(maximum_subarray(nums4))


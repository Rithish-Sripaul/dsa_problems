def first_approach(nums):
    if len(nums) == 1:
        return nums[0]
    
    low, high = 0, len(nums) - 1
    sum_ = 0
    
    while low <= high:
        middle = (low + high) // 2

        if middle == 0:
            return nums[0]

        if middle == len(nums) - 1:
            return nums[-1]

        if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
            return nums[middle]
        elif (middle % 2 == 0 and nums[middle] == nums[middle + 1]) or (middle % 2 == 1 and nums[middle] != nums[middle + 1]):
            low = middle + 1
        else:
            high = middle - 1

            
        # if middle % 2 == 1:
            # high = middle - 1
        # else:
            # low = middle + 1
    
    return nums[middle]

nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
nums1 = [3, 3, 7, 7, 10, 11, 11]

print(first_approach(nums))
print(first_approach(nums1))
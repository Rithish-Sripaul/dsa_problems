def first_approach(nums, target):
    lower_bnd = len(nums)

    low, high = 0, len(nums) - 1
    
    while low <= high:
        middle = (low + high) // 2

        if nums[middle] >= target:
            high = middle - 1
            lower_bnd = middle
        else:
            low = middle + 1
    return lower_bnd

nums = [1, 2, 2, 3]
nums1 = [3, 5, 8, 15, 19]
print(first_approach(nums, 2))
print(first_approach(nums1, 9))

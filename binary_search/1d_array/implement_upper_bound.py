def first_approach(nums, target):
    upper_bnd = -1

    low, high = 0, len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        if nums[middle] > target:
            upper_bnd = middle
            high = middle - 1
        else:
            low = middle + 1
    
    return upper_bnd
nums = [1, 2, 2, 3]
nums1 = [3, 5, 8, 9, 15, 19]
print(first_approach(nums, 2))
print(first_approach(nums1, 9))
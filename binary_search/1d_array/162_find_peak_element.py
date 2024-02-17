def first_approach(nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1 
    low, high = 0, len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        
        if nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
            return middle
        
        if nums[middle] < nums[middle + 1]:
            low = middle + 1
        else:
            high = middle - 1

nums = [1, 2, 3, 1]
nums1 = [1, 2, 1, 3, 5, 6, 4]

print(first_approach(nums))
print(first_approach(nums1))
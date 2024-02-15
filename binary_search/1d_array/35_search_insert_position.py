def first_approach(nums, low, high, target):
    middle = (high + low) // 2

    if high >= low:
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return first_approach(nums, low, middle - 1, target)
        else:
            return first_approach(nums, middle + 1, high, target)
    else:
        return middle + 1
    
nums = [1, 3, 5, 6]
print(first_approach(nums, 0, len(nums) - 1, 5))
print(first_approach(nums, 0, len(nums) - 1, 2))
print(first_approach(nums, 0, len(nums) - 1, 7))
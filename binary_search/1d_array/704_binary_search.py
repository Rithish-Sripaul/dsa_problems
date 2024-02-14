def binary_search(nums, low, high, target):
    middle = (high + low) // 2

    if high >= low:
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            return binary_search(nums, low, middle - 1, target)
        else:
            return binary_search(nums, middle + 1, high, target)
    else:
        reutrn -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(nums, 0, len(nums) - 1, target))

def first_approach(nums, target):

    # Upper bound
    upperBound = len(nums)
    low, high = 0, len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        if nums[middle] > target:
            upperBound = middle
            high = middle - 1
        else:
            low = middle + 1
    
    # Lower bound
    lowerBound = 0
    low, high = 0, len(nums) - 1
    elementThere = False
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] >= target:
            lowerBound = middle
            high = middle - 1
        else:
            low = middle + 1
    if lowerBound == len(nums) or nums[lowerBound] != target:
        return [-1, -1]
    return [lowerBound, upperBound - 1] 
nums = [5, 7, 7, 8, 8, 10]
print(first_approach(nums, 8))
print(first_approach([2, 2], 2))

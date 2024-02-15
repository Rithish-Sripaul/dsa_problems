# Count the number of occurunces of element in sorted array

def first_approach(nums, target):
    # ans = upperBound - lowerBound + 1

    # LOWER BOUND
    lowerBound = -1
    low, high = 0, len(nums) - 1

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] >= target:
            lowerBound = middle
            high = middle - 1
        else:
            low = middle + 1

    # UPPER BOUND
    upperBound = -1
    low, high = 0, len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if nums[middle] > target:
            upperBound = middle
            high = middle - 1
        else:
            low = middle + 1
    
    if lowerBound == -1:
        return 0
    if upperBound == -1:
        return 1
    
    return upperBound - lowerBound 

nums = [2, 2, 3, 3, 3, 3, 4]
nums1 = [1, 2, 3, 3, 3, 3, 5, 10]
print(first_approach(nums1, 12))
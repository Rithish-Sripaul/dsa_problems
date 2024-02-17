def first_approach(nums):
    low, high = 0, len(nums) - 1
    minTillNow = 99999999
    while low <= high: 
        middle = (low + high) // 2
        
        if nums[middle] <= minTillNow:
            minTillNow = nums[middle]
        
        if nums[low] <= nums[middle]:
            # left side is the sorted half
            if nums[high] <= nums[low]:
                low = middle + 1
            else:
                high = middle - 1
        else:
            if nums[high] <= nums[middle]:
                low = middle + 1
            else:
                high = middle - 1
    
    return minTillNow

nums = [3, 4, 5, 1, 2]
nums1 = [4, 5, 6, 7, 0, 1, 2]
nums2 = [11, 13, 15, 17]
print(first_approach(nums))
print(first_approach(nums1))
print(first_approach(nums2))


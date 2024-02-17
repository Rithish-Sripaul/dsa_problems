def first_approach(nums):
    low, high = 0, len(nums) - 1
    minEle = 5001
    minInd = 0

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] <= minEle:
            minEle = nums[middle]
            minInd = middle
        
        if nums[low] <= nums[middle]:
            if nums[high] <= nums[low]:
                low = middle + 1
            else:
                high = middle - 1
        else:
            if nums[high] <= nums[middle]:
                low = middle + 1
            else:
                high = middle - 1
        
    return minInd

nums = [4, 5, 6, 7, 0, 1, 2]
nums1 = [4, 5, 6, 7]
nums2 = [3, 4, 5, 1, 2]
print(first_approach(nums))
print(first_approach(nums1))
print(first_approach(nums2))

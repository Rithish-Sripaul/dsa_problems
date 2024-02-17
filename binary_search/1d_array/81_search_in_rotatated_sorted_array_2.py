def first_appriach(nums, target):
    low, high = 0, len(nums) - 1

    # find k, the index at which the second sorted half starts
    # we will do this with binary search -> O(logn)


    while low <= high:
        middle = (low + high)//2
        
        if nums[middle] == target:
            return True
        # Edge case where nums[low] == nums[middle] == nums[high]
        elif nums[low] == nums[middle] == nums[high]:
            high -= 1
            low += 1
        elif nums[low] <= nums[middle]:
            if nums[low] <= target and target <= nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
        else:
            if nums[middle] <= target and target <= nums[high]:
                low = middle + 1
            else:
                high = middle - 1
        
    return False

nums = [2,5,6,0,0,1,2]
nums1 = [1, 0, 1, 1, 1]

print(first_appriach(nums, 3))
print(first_appriach(nums1, 0))
        
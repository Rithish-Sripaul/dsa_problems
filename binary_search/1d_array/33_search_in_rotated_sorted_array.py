def first_approach(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high: 
        middle = (low + high) // 2

        if nums[middle] == target:
            return middle
        # to get the sorted half of the array
        elif nums[low] <= nums[middle]:
            # The left side is the sorrted half

            # the target is in the left half
            if nums[low] <= target and target <= nums[middle]:
                high = middle - 1
            # the target is in the right hald
            else:
                low = middle + 1

        else:
            # the right half is the sorted array
            if nums[middle] <= target and target <= nums[high]:
                low = middle + 1
            else:
                high = middle - 1
    return - 1


nums = [4, 5, 6, 7, 0, 1, 2]
nums2 = [9, 1, 2, 3, 4, 5, 6, 7, 8]
nums1 = [3, 1]
print(first_approach(nums, 3))
print(first_approach(nums1, 1))
print(first_approach(nums2, 9))
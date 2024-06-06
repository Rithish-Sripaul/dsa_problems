def search_rotatedtwo(nums, target):
  low, high = 0, len(nums) - 1

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] == target:
      return True
    elif nums[low] == nums[middle] == nums[high]:
      low += 1
      high -= 1
    else:
      if nums[low] <= nums[middle]:
        # Left part is sorted

        if nums[low] <= target and target <= nums[middle]:
          high = middle - 1
        else:
          low = middle + 1
      else:
        # Left part is not sorted

        if nums[middle] <= target and target <= nums[high]:
          low = middle + 1
        else:
          high = middle - 1
  return False

nums = [2, 5, 6, 0, 0, 1, 2]
print(search_rotatedtwo(nums, 2))
def search_rotated(nums, target):
  low, high = 0, len(nums) - 1

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] == target:
      return middle
    
    if nums[low] < nums[middle]:
      # The left part of the array is sorted

      # Now to check on which side the target might be

      if nums[low] <= target and target < nums[middle]:
        high = middle - 1
      else:
        low = middle + 1
    else:
      if nums[middle] < target and target <= nums[high]:
        low = middle + 1
      else:
        high = middle - 1
  return -1

nums = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(nums, 0))
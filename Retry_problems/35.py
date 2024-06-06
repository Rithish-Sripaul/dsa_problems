def searchPosition(nums, target, low, high):
  middle = (low + high) // 2
  if low <= high:
    if nums[middle] == target:
      return middle
    elif nums[middle] > target:
      return searchPosition(nums, target, low, middle - 1)
    else:
      return searchPosition(nums, target, middle + 1, high)
  return middle + 1

nums = [1, 3, 5, 6]
print(searchPosition(nums, 2, 0, len(nums) - 1))
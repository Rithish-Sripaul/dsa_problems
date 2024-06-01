def binarySearch(nums, target):

  low, high = 0, len(nums)
  while low <= high:
    middle = (low + high) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] > target:
      high = middle - 1
    else:
      low = middle + 1
  return -1

nums = [-1, 0, 3, 5, 9, 12]
print(binarySearch(nums, 9))
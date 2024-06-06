def implement_upper_bound(nums, target):
  low, high, upper_bound = 0, len(nums) - 1, 0

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] > target:
      high = middle - 1
      upper_bound = middle
    else:
      low = middle + 1
  return upper_bound

nums = [1, 2, 2, 3]
print(implement_upper_bound(nums, 2))

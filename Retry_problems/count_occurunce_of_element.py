def first_last_pos(nums, target):

  # First Position - floor

  low, high = 0, len(nums) - 1
  floor = len(nums)

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] >= target:
      high = middle - 1
      floor = middle
    else:
      low = middle + 1
  
  low, high, ceil = 0, len(nums) - 1, len(nums)
  while low <= high:
    middle = (low + high) // 2

    if nums[middle] <= target:
      low = middle + 1
      ceil = middle
    else:
      high = middle - 1
  
  if floor == len(nums) or nums[floor] != target:
    return 0
  return ceil - floor + 1
  
nums = [5, 7, 7, 8, 8, 10]
print(first_last_pos(nums, 4))
print(first_last_pos([1, 2, 3], 1))
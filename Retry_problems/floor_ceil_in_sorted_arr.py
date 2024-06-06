def floor_ceil(nums, target):
  low, high, floor, ceil = 0, len(nums) - 1, len(nums), len(nums)

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] <= target:
      floor = middle
      low = middle + 1
    else:
      high = middle - 1

  
  low, high = 0, len(nums) - 1
  while low <= high:
    middle = (low + high)//2
    if nums[middle] >= target:
      high = middle - 1
      ceil = middle
    else:
      low = middle + 1
  
  print(nums[floor], nums[ceil])

floor_ceil([3, 4, 4, 7, 8, 10], 5)
floor_ceil([3, 4, 4, 7, 8, 10], 8)
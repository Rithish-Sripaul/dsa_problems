def findFloor(nums, target):
  low, high = 0, len(nums) - 1
  floor = len(nums)

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] <= target:
      floor = middle
      low = middle + 1
    else:
      high = middle - 1
  return floor

def findCeil(nums, target):
  low, high = 0, len(nums) - 1
  ceil = len(nums)

  while low <= high:
    middle = (low + high) // 2
    if nums[middle] >= target:
      ceil = middle
      high = middle - 1
    else:
      low = middle + 1
  
  return ceil

def findFloorCeil(nums, target):
  print(findFloor(nums, target), findCeil(nums, target))

nums = [3, 4, 4, 7, 8, 10]
target = 4
findFloorCeil(nums, target)
def first_approach(nums, target):
  upperBound = len(nums)
  low, high = 0, len(nums) - 1

  while low <= high: 
    middle = (low + high) // 2

    if nums[middle] > target:
      upperBound = middle
      high = middle - 1
    else:
      low = middle + 1
    
  lowerBound = 0
  low, high = 0, len(nums) - 1

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] >= target:
      lowerBound = middle
      high = middle - 1
    else:
      low = middle + 1
  
  return upperBound - lowerBound

nums = [1, 22, 33, 33, 33, 44, 122]
print(first_approach(nums, 44))
  
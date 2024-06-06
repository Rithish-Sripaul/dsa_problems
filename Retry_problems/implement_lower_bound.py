def find_lower_bound(nums, target):
  low, high, lower_bound = 0, len(nums) - 1, 0

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] >= target:
      high = middle - 1
      lower_bound = middle
    else:
      low = middle + 1
    
  return lower_bound

nums = [3, 5, 8, 15, 19]
print(find_lower_bound(nums, 9))

# Recursion Method
def lower_bound(nums, target, low, high, lower_b):
  if low <= high:
    middle = (low + high) // 2

    if nums[middle] >= target:
      return lower_bound(nums, target, low, middle - 1, middle)
    else:
      return lower_bound(nums, target, middle + 1, high, lower_b)
  return lower_b

print(lower_bound(nums, 9, 0, len(nums) - 1, 0))
  
  


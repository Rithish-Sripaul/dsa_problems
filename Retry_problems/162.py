def peak_element(nums):
  if len(nums) == 1:
    return 0
  if nums[0] > nums[1]:
    return 0
  if nums[-1] > nums[-2]:
    return len(nums) - 1
  
  low, high = 0, len(nums) - 1

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] > nums[middle - 1] and nums[middle] > nums[middle + 1]:
      return middle
    
    if nums[middle] < nums[middle + 1]:
      low = middle + 1
    else:
      high = middle - 1

print(peak_element([9, 2]))
print(peak_element([3, 4, 3, 2, 1]))

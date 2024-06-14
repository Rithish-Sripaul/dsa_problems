def find(nums, k):
  left = right = 0

  for right in range(len(nums)):
    if nums[right] % 2 == 1:
      k -= 1
    
    if k < 0:
      if nums[left] % 2 == 1:
        k += 1
      left += 1
  
  return right - left + 1

print(find([2,2,2,1,2,2,1,2,2,2], 2))
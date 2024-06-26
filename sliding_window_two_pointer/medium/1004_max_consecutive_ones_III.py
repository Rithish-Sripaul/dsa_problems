def find(nums, k):
  left = right = 0

  for right in range(len(nums)):
    if nums[right] == 0:
      k -= 1
    
    if k < 0:
      if nums[left] == 0:
        k += 1
      left += 1
  
  return right - left + 1
print(find([1,1,1,0,0,0,1,1,1,1,0], 2))
print(find([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))




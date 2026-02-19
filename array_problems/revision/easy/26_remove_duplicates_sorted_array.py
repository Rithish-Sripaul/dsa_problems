def solution(nums):
  if len(nums) == 1:
    return 1
  current_ele, current_pos = nums[0], 1
  count = 1
  for i in range(1, len(nums)):
    if nums[i] != current_ele:
      nums[current_pos] = nums[i]
      current_ele = nums[i]
      current_pos += 1
      
  
  return current_pos

print(solution([1, 1, 1, 2, 3, 3, 3]))




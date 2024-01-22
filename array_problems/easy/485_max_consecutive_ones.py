def max_consecutive_ones(nums):
  max_streak = 0
  current_streak = 0
  for i in range(len(nums)):
    if nums[i] == 1:
      current_streak += 1
    else:
      max_streak = max(max_streak, current_streak)
      current_streak = 0
    
  return max(max_streak, current_streak)

nums = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
print(max_consecutive_ones(nums))

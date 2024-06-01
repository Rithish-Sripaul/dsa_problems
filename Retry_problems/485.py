def max_consecutive(nums):
  curr, max_count = 0, 0

  for i in nums:
    if i == 1:
      curr += 1
    else:
      max_count = max(curr, max_count)
      curr = 0
  return max(max_count, curr)

nums = [1, 1, 0, 1, 1, 1]
print(max_consecutive(nums))
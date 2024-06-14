def find(nums):
  stack = []
  result = [-1] * len(nums)

  for idx in range((len(nums) * 2) - 1, -1, -1):
    i = idx % len(nums)
    while stack and stack[-1] <= nums[i]:
      stack.pop()
    
    if stack:
      result[i] = stack[-1]

    else:
      result[i] = -1
    stack.append(nums[i])
  return result
nums = [1, 2, 3, 4, 3]
#nums = [1, 2,1]
print(find(nums))



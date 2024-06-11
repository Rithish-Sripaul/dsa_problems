def smaller_on_left(nums):
  stack = []
  result = []

  for i in range(len(nums)):
    while stack and stack[-1] >= nums[i]:
      stack.pop()
    
    if stack:
      result.append(stack[-1])
    else:
      result.append(-1)
    stack.append(nums[i])
  
  return result

print(smaller_on_left([2, 3, 4, 5, 1]))
print(smaller_on_left([4, 8, 5, 2, 25]))
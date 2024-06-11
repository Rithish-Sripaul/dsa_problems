def nextGreaterElement(nums):
  stack = []
  result = []

  for i in range(len(nums) - 1, -1, -1):
    while stack and stack[-1] < nums[i]:
      stack.pop()

    if stack:
      result.insert(0, stack[-1])
    else:
      result.insert(0, -1)
    stack.append(nums[i])
  return result

print(nextGreaterElement([4, 5, 2, 25]))
print(nextGreaterElement([13, 7, 6, 12]))
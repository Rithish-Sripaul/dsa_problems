def find(nums):
  stack = []
  resultGreater = []

  for i in range(len(nums) - 1, -1, -1):
    while stack and nums[stack[-1]] < nums[i]:
      stack.pop()

    if stack:
      resultGreater.insert(0, stack[-1])
    else:
      resultGreater.insert(0, -1)
    stack.append(i)


  stack, resultSmaller = [], []
  for i in range(len(nums) -1, -1, -1):
    while stack and nums[stack[-1]] >= nums[i]:
      stack.pop()

    if stack:
      resultSmaller.insert(0, nums[stack[-1]])
    else:
      resultSmaller.insert(0, -1)
    stack.append(i)


  ans = []
  for i in resultGreater:
    ans.append(resultSmaller[i])

  return ans

print(find([5, 1, 9, 2, 5, 1, 7]))

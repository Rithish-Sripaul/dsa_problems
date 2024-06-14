def sumOfSubarrayRanges(nums):
  s = 0
  stack = []
  res = []
  for i in range(len(nums) - 1, -1, -1):
    N = len(nums) - i - 1

    s += nums[i]
    while stack and stack[-1] > nums[i]:
      stack.pop()
  
    if stack:
      s += N * stack[-1]
      res.insert(0, stack[-1])
    else:
      s += N * nums[i]
      res.insert(0, nums[i])
    stack.append(nums[i])

  return s


print(sumOfSubarrayRanges([3, 1, 2, 4]))
print(sumOfSubarrayRanges([11,81,94,43,3]))
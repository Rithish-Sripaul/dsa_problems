def maximum_subarray(nums):
  result = sum(nums)
  crntSum = 0

  for i in nums:
    crntSum += i
    if crntSum > result:
      result = crntSum
    if crntSum < 0:
      crntSum = 0
  return result
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray(nums))
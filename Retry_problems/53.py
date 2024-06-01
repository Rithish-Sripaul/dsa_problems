def maximum_subarray(nums):
  result = nums[0]
  sum_ = 0

  for i in nums:
    sum_ += i
    if sum_ > result:
      result = sum_
    if sum_ < 0:
      sum_ = 0
  return max(result, sum_)
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray(nums))
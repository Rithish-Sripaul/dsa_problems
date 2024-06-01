def single_number(nums):
  n = 0
  for i in nums:
    n = n ^ i
  return n
nums = [4, 1, 2, 1, 2]
nums = [1]
print(single_number(nums))
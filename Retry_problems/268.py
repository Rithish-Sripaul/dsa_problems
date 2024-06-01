def missing_number(nums):
  n = len(nums)
  total = (n*(n+1))/2
  for i in nums:
    total -= i
  return int(total)

nums = [9,6,4,2,3,5,7,0,1]
nums = [0, 1, 3]
print(missing_number(nums))
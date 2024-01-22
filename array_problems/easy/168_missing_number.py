def missing_number(nums):
  n = len(nums)
  sum_naturual = (n * (n + 1)) / 2

  for i in nums:
    sum_naturual -= i
  
  return int(sum_naturual)

nums = [9,6,4,2,3,5,7,0,1]
print(missing_number(nums))
def subsetSums(index, s):
  if index == len(nums):
    res.append(s)
    return
  res.append(s)
  for i in range(index, len(nums)):
    if i > index and nums[i] == nums[i - 1]:
      continue
    subsetSums(i + 1, s + nums[i])
  
nums = [5, 2, 1]
res = []
subsetSums(0, 0)
print(res)
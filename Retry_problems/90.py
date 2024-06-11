  def subsets2(index, path):
    if len(path) == len(nums):
      res.append(path)
      return
    
    res.append(path)
    for i in range(index, len(nums)):
      if i > index and nums[i] == nums[i - 1]:
        continue
      subsets2(i + 1, path + [nums[i]])

nums = [1, 2, 2]
res = []
subsets2(0, [])
print(res)

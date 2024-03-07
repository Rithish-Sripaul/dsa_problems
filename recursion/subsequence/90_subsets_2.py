def find(index, path):

  res.append(path)
  if len(path) == len(nums): return

  for i in range(index, len(nums)):
    if i > index and nums[i] == nums[i - 1]:
      continue
    find(i + 1, path + [nums[i]])

res = []
nums = [1, 2, 2]
find(0, [])
print(res)
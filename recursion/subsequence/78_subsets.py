def find(index, path):
  if len(res) == 2 * len(nums): return

  if len(path) == len(nums):
    res.append(path)
    return
  res.append(path)
  for i in range(index, len(nums)):
    find(i + 1, path + [nums[i]])



res = []
nums = [1, 2, 3]
find(0, [])
print(res)
printS(0, [])
  
res = []
nums = [0]
find(0, [])
print(res)
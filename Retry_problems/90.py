def subsets2(index, path):
  if len(path) == len(nums):
    res.append(path)
    return
  
  res.append(path)
  for i in range(index, len(nums)):
    if i > index and nums[i] == nums[i - 1]:
      continue
    subsets2(i + 1, path + [nums[i]])

def subsets21(index, path):
  if index == len(nums):
    res.add(tuple(path))
    return
  
  path.append(nums[index])
  subsets21(index + 1, path)
  path.pop()
  subsets21(index + 1, path)

nums = [1, 2, 2]
res = set()
subsets21(0, [])
print(res)

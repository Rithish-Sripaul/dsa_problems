def find(index, sum, path):
  if sum > target: return
  if sum == target: 
    res.append(path)
    return

  for i in range(index, len(nums)):
    if i > index and nums[i] == nums[i - 1]:
      continue
    find(i + 1, sum + nums[i], path + [nums[i]])
res = []
path = []
nums = [10, 1, 2, 7, 6, 1, 5]
nums.sort()
target = 8
find(0, 0, [])
print(res)
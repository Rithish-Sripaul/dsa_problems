def find(sum_, index, path):
  if sum_ > target: return

  if sum_ == target:
    res.add(  path)
    return

  for i in range(index, len(nums)):
    find(sum_ + nums[i], i + 1, path + [nums[i]])
  
res = set()
nums = [1, 2, 3, 1, 1, 1]
target = 3
find(0, 0, [])
print(res)
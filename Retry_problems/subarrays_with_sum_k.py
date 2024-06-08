def find(sum_, index, path):
  if sum_ == n:
    res.append(path)
    return
  elif sum_ > n or index == len(nums):
    return
  if len(res) == 0:
    for i in range(index, len(nums)):
      find(sum_ + nums[i], i + 1, path + [nums[i]])

def printS(index, s, sum_, nums, ds):
  if index == len(nums):
    if s == sum_:
      ans = []
      for _ in ds: ans.append(_)
      res.append(ans)
    return
  
  s += nums[index]
  ds.append(nums[index])

  printS(index + 1, s, sum_, nums, ds)

  s -= nums[index]
  ds.pop()

  printS(index + 1, s, sum_, nums, ds)

def printS_one(index, s, sum_, nums, ds):

  if index == len(nums):
    if s == sum_:
      ans = []
      for _ in ds: ans.append(_)
      res.append(ans)
      return True
    return False

  s += nums[index]
  ds.append(nums[index])

  if printS_one(index + 1, s, sum_, nums, ds): return True

  s -= nums[index]
  ds.pop()

  if printS_one(index + 1, s, sum_, nums, ds): return True

  return False
    

res = []
nums = [1, 2, 1]
n = 2
#find(0, 0, [])
printS(0, 0, n, nums, [])
print(res)

print(printS_one(0, 0, 5, nums, []))
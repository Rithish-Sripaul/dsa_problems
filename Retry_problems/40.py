def combinationSumDFS(index, path, s):
  if s > target:
    return
  if s == target:
    res.append(path)
    return
  
  for i in range(index, len(nums)):
    combinationSumDFS(i + 1, path + [nums[i]], s + nums[i])

def combinationSum(index, path, s, nums, target, ds):
  if index == len(nums):
    if s == target:
      print(ds)
    return
  

  if arr[ind] <= target:
    s += nums[index]
    ds.append(nums[index])
    combinationSum(index + 1, path, s, nums, target, ds)

  s -= nums[index]
  ds.pop()

  combinationSum(index + 1, path, s, nums, target, ds)

nums = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = []
combinationSum(0, [], 0, sorted(nums), target, [])
print(res)
def find(sum, index, target, s):
  if sum > target: return
  if sum == target: 
    res.append(s)
    return
  for i in range(index, len(nums)):
    find(sum + nums[i], i, target, s + [nums[i]])

res = []
nums = [2, 3, 6, 7]
find(0, 0, 7, [])
print(res)

res = []
nums = [2, 3, 5]
find(0, 0, 8, [])
print(res)

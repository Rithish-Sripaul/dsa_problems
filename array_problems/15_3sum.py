def threeSum(nums):
  hash = {}
  ans = []
  for i in range(len(nums)):
    if nums[i] in hash:
      continue
    start = nums[i]
    # Two Sum
    target = -start
    secondHash = {}
    for j in range(i, len(nums)):
      if target - nums[j] in secondHash:
        hash[nums[i]] = hash.get(nums[i], 0) + 1
        hash[nums[j]] = hash.get(nums[j], 0) + 1
        hash[nums[target - nums[j]]] = hash.get(nums[target - nums[j]], 0) + 1
        ans.append([nums[i], nums[j], nums[target - nums[j]]])
        break
      else:
        hash[nums[j]] = j
  return ans

print(threeSum([-1,0,1,2,-1,-4]))

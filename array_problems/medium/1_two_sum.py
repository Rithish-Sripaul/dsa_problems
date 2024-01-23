def two_sum(nums, target):
  hash = {}
  for i in range(len(nums)):
    if target - nums[i] in hash:
      return [i, hash[target - nums[i]]]
    
    hash[nums[i]] = hash.get(nums[i], 0) + i
      
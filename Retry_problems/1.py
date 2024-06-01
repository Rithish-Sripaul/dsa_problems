def two_sum(nums, target):
  hash = {}
  for i in range(len(nums)):
    if target - nums[i] in hash:
      return [i, hash[target - nums[i]]]
    else:
      hash[nums[i]] = i
    
nums = [2, 7, 11, 15]
print(two_sum(nums, 9))
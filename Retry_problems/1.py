def two_sum(nums, target):
  prev_diff = {}

  for i in range(len(nums)):
    if target - nums[i] in prev_diff.keys():
      return [i, prev_diff[target - nums[i]]]
    prev_diff[nums[i]] = i

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))

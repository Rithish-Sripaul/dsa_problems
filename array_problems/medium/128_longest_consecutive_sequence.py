# 128 - Longest Consecutive Sequence

def first_approach_with_dict(nums):
  hash = {}
  maxTillNow = 0

  for i in range(len(nums)):
    if nums[i] in hash:
      hash[nums[i]] += 1
    else:
      hash[nums[i]] = 1
  
  for i in range(len(nums)):
    if nums[i] - 1 not in hash:
      # Starting point -> nums[i]
      crnt = 0
      start = nums[i]
      while start in hash:
        crnt += 1
        start += 1
      maxTillNow = max(maxTillNow, crnt)

  return maxTillNow


def optimal_approach_with_set(nums):
  nums = set(nums)
  max_till_now = 0

  for x in nums:
    if x - 1 not in nums:
      y = x + 1
      while y in nums:
        y += 1
      max_till_now = max(max_till_now, y - x)

  return max_till_now
nums = [4,1,3,2]
print(optimal_approach_with_set(nums))
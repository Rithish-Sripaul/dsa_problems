def longestIncreasingSubsqnce(nums):
  maxCount, crntCount = 0, 0
  crntNum = nums[0]
  for i in range(1, len(nums)):
    if nums[i] > crntNum:
      crntCount += 1
    else:
      maxCount = max(maxCount, crntCount)
      crntCount = 1
    crntNum = nums[i]
  return max(crntCount, maxCount)

nums = [10,9,2,5,3,7,101,18]
print(longestIncreasingSubsqnce(nums))
nums = [0,1,0,3,2,3]
print(longestIncreasingSubsqnce(nums))

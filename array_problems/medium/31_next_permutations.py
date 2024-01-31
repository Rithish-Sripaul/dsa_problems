# 31 - Next Permutations

def first_approach(nums):
  highestPeakInd = 0
  highestPeakEle = -1
  for i in range(len(nums)):
    if nums[i] >= highestPeakEle:
      highestPeakEle = nums[i]
      highestPeakInd = i
  
  # Special case: The list is in descending order
  if highestPeakEle == 0:
    print(nums.sorted())
    return
  
  nearestSmallestEleInd = highestPeakInd - 1
  while nearestSmallestEleInd >= 0:
    if nums[nearestSmallestEleInd] < highestPeakEle:
      break
    nearestSmallestEleInd -= 1

  # Special Case 2: An element greater than nearestSmallestEle in the descending side after the highest peak
  eleGreaterNearestSmall = False
  i = highestPeakInd + 1
  while i < len(nums):
    if nums[i] > nums[nearestSmallestEleInd]:
      eleGreaterNearestSmall = True
      nums[i], nums[nearestSmallestEleInd] = nums[nearestSmallestEleInd], nums[i]
      nums[nearestSmallestEleInd + 1:] = sorted(nums[nearestSmallestEleInd + 1:])
      break
    i += 1
  
  if not eleGreaterNearestSmall:
    nums[nearestSmallestEleInd], nums[highestPeakInd] = nums[highestPeakInd], nums[nearestSmallestEleInd]
    nums[highestPeakInd:] = sorted(nums[highestPeakInd:])
  print(nums)

nums = [1, 2, 3]
nums = [1, 1, 5]
nums = [2, 3, 1]
# nums = [1, 2, 3, 4, 3, 2, 3, 4, 2]
# nums = [1, 3, 2]
first_approach(nums) 
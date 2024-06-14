def find(nums, goal):
  if goal < 0: return 0

  left, right = 0, 0
  s, cut = 0, 0

  while right <= len(nums) - 1:
    s += nums[right]
    while s > goal:
      s -= nums[left]
      left += 1
    cut = cut + (right - left + 1)
    right += 1
  return cut

def binarySubarraysWithSum():
  nums = [1, 0, 1, 0, 1]
  goal = 2
  cut1, cut2 = find(nums, goal), find(nums, goal - 1)
  return cut1 - cut2

print(binarySubarraysWithSum())


def longestConsecutive(nums: list[int]) -> int:
  nums = set(nums)
  maxTillNow = 0

  for x in nums:
    # To find the starting point of the sequence
    if x - 1 not in nums:
      y = x + 1
      while y in nums:
        y += 1
      maxTillNow = max(maxTillNow, y - x)
  return maxTillNow
# 128 - Longest Consecutive Sequence

def first_approach(nums):
  hash = {}
  maxTillNow = 0
  currTillNow = 0
  for i in range(len(nums)):
    for i 
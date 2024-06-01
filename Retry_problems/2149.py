def rearrrange(nums):
  pos, neg, count = 0, 0, 0
  ans = [0] * len(nums)

  while count < len(nums):
    if count % 2 == 0:
      while nums[pos] < 0:
        pos += 1
      ans[count] = nums[pos]
      pos += 1
    else:
      while nums[neg] >= 0:
        neg += 1
      ans[count] = nums[neg]
      neg += 1
    count += 1
  return ans

nums = [3, 1, -2, -5, 2, -4]
print(rearrrange(nums))

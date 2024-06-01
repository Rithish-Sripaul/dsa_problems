def move_zeroes(nums):
  l, r = 0, 0
  while l < len(nums) and r < len(nums):
    if nums[l] == 0:
      if nums[r] != 0:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r += 1
      else:
        r += 1
    else:
      l += 1
      r += 1
  return nums

nums = [1, 0, 0, 3]
nums1 = [1, 0]
print(move_zeroes(nums1 ))


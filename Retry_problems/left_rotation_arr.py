def left_rotate(nums, n):
  for _ in range(n):
    last = nums[0]
    for i in range(len(nums) - 1):
      nums[i] = nums[i + 1]
    nums[-1] = last
  return nums

nums = [1, 2, 3, 4]
print(left_rotate(nums, 2))
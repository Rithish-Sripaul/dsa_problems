def rotate_array(nums, n):
  for _ in range(n):
    last = nums[-1  ]
    for i in range(len(nums) - 1, 0, -1):
      nums[i] = nums[i - 1]
    nums[0] = last
  return nums

nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 2)
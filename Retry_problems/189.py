def rotate_array(nums, n):
  for _ in range(n):
    last = nums[-1  ]
    for i in range(len(nums) - 1, 0, -1):
      nums[i] = nums[i - 1]
    nums[0] = last
  return nums

nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array(nums, 2)

def rotate_arary_2025(nums, k):
  if len(nums) == 1:
    return nums
  

  for count in range(k):
    lastEle = nums[-1]
  
    for i in range(len(nums) - 1, -1, -1):
      nums[i] = nums[i - 1]
    nums[0] = lastEle
    print(nums)
print(rotate_arary_2025([1, 2, 3, 4, 5, 6, 7], 3))

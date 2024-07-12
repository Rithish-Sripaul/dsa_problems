def find(nums, k):
  n = len(nums)


  left, right = 0, 0
  count, cut = 0, 0

  while right < len(nums):
    if nums[right] % 2 == 1: count += 1

    while count > k:
      if nums[left] % 2 == 1: count -= 1
      left += 1

    cut = cut + (right - left + 1)
    right += 1
  return cut

nums = [1, 1, 2, 1, 1]
k = 3
print(find(nums, k) - find(nums, k - 1))

nums = [2, 4, 6]
k = 1
print(find(nums, k) - find(nums, k - 1))

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(find(nums, k) - find(nums, k - 1))

nums = [1, 1, 1, 1, 1]
k = 1
print(find(nums, k) - find(nums, k - 1))




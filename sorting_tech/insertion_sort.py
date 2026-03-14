def insertion_sort(nums):
  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and key < nums[j]:
      nums[j + 1] = nums[j]
      j -= 1
    nums[j + 1] = key
  return nums
nums = [2, 0, -1, 100, 450, 300, -100]
insertion_sort(nums)
print(nums)
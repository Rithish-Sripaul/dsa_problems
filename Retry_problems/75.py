def sort_colors(nums):
  low, mid, high = 0, 0, len(nums) - 1

  while mid <= high:
    if nums[mid] == 0:
      nums[mid], nums[low] = nums[low], nums[mid]
      mid += 1
      low += 1
    elif nums[mid] == 2:
      nums[mid], nums[high] = nums[high], nums[mid]

      high -= 1
    else:
      mid += 1
  return nums

nums = [2, 2, 1, 0, 1, 0]
print(sort_colors(nums))

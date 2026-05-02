def swap(i, j, nums):
  nums[i], nums[j] = nums[j], nums[i]

def sort_colors(nums):
  left, mid, right = 0, 0, len(nums) - 1

  while mid <= right:
    if nums[mid] == 0:
      swap(mid, left, nums)
      left += 1
      mid += 1
    elif nums[mid] == 2:
      swap(mid, right, nums)
      right -= 1
    else:
      mid += 1

  return nums

nums = [2, 0, 1, 1, 2, 0]
sort_colors(nums)
print(nums)
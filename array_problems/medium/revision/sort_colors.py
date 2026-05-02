
def sort_colors(nums):
  left, mid, right = 0, 0, len(nums) - 1

  while mid <= right:
    if nums[mid] == 0:
      nums[left], nums[mid] = nums[mid], nums[left]
      left += 1
      mid += 1
    elif nums[mid] == 2:
      nums[right], nums[mid] = nums[mid], nums[right]
      right -= 1
      
    else:
      mid += 1

nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums)
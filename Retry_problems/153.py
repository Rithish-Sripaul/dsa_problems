# Find minimum in rotated sorted array

def find_minimum(nums):
  min_nums = nums[0]

  low, high = 0, len(nums) - 1

  while low <= high:
    middle = (low + high) // 2

    if nums[middle] <= min_nums:
      min_nums = nums[middle]

    if nums[low] <= nums[middle]:
      # Left side is sorted

      if nums[high] <= nums[low]:
        low = middle + 1
      else:
        high = middle - 1
    else:
      # Right side is sorted

      if nums[high] <= nums[middle]:
        low = middle + 1
      else:
        high = middle - 1
  return min_nums

print(find_minimum([3, 4, 5, 1, 2]))
print(find_minimum([4, 5, 6, 7, 8, 0, 1, 2]))

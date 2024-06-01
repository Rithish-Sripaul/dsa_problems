# Iterative Approach

def binarySearchIter(nums, target):

  low, high = 0, len(nums)
  while low <= high:
    middle = (low + high) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] > target:
      high = middle - 1
    else:
      low = middle + 1
  return -1

nums = [-1, 0, 3, 5, 9, 12]


def binarySearch(nums, target, low, high):


  if high >= low:
    middle = (low + high) // 2
    if nums[middle] == target:
      return middle
    elif nums[middle] > target:
      return binarySearch(nums, target, low, middle - 1)
    else:
      return binarySearch(nums, target, middle + 1, high)
  return -1
print(binarySearch(nums, 3, 0, len(nums) - 1))

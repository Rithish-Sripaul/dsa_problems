def partition(low, high, nums):

  # choosing the right most pivot
  pivot = nums[high]

  i = low - 1

  for j in range(low, high):
    if nums[j] < pivot:
      i += 1
      swap(i , j, nums)
  
  swap(i + 1, high, nums)
  return i + 1

def swap(i, j, nums):
  nums[i], nums[j] = nums[j], nums[i]

def quickSort(low, high, nums):
  if low < high:
    pi = partition(low, high, nums)

    quickSort(low, pi - 1, nums)
    quickSort(pi + 1, high, nums)

nums = [2, 0, 1, 4, 5, 3]
quickSort(0, len(nums) - 1, nums)
print(nums)


  
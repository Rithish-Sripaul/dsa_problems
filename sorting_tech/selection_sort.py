def selection_sort(nums):

  for ind in range(len(nums)):
    for i in range(ind + 1, len(nums)):
      if nums[i] < nums[ind]:
        nums[i], nums[ind] = nums[ind], nums[i]
  
  return nums


def selection_sort_desc(nums):

  for ind in range(len(nums)):
    for i in range(ind + 1, len(nums)):
      if nums[i] > nums[ind]:
        nums[i], nums[ind] = nums[ind], nums[i]
  return nums

def selection_sort_largest(nums):
  for ind in range(len(nums) - 1, -1, -1):
    for i in range(len(nums) - 1, ind - 1, -1):
      if nums[i] < nums[ind]:
        nums[i], nums[ind] = nums[ind], nums[i]
  return nums

def selection_sort_largest_desc(nums):
  for ind in range(len(nums) - 1, -1, -1):
    for i in range(len(nums) - 1, ind - 1, -1):
      if nums[i] > nums[ind]:
        nums[i], nums[ind] = nums[ind], nums[i]
  return nums

  
nums = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selection_sort(nums)
print(nums)

selection_sort_desc(nums)
print(nums)

selection_sort_largest(nums)
print(nums)

selection_sort_largest_desc(nums)
print(nums)
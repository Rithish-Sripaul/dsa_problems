def selection_sort(nums):

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[i]:
        nums[j], nums[i] = nums[i], nums[j]
  
  return nums

def bubble_sort(nums):
  for i in range(len(nums) - 1, 0, -1):
    swapped = False
    for j in range(i):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        swapped = True
    if not swapped:
      break
  return nums


nums = [0, -1, 2, 100, 300, -100, 450]
bubble_sort(nums)
print(nums)
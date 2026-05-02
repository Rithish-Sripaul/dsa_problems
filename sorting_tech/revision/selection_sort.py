def swap(i, j, nums):
  nums[j], nums[i] = nums[i], nums[j]

def selection_sort(nums):

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[i]:
        nums[j], nums[i] = nums[i], nums[j]


def bubble_sort(nums):
  for i in range(len(nums) - 1, 0, -1):
    swapped = False
    for j in range(i):
      if nums[j] > nums[j + 1]:
        swapped = True
        swap(j, j + 1, nums)

    if not swapped:
      break

def insertion_sort(nums):
  for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
      nums[j + 1] = nums[j]
      j -= 1
    nums[j + 1] = key



nums = [3, 2, 1, 0, 4, 5]
insertion_sort(nums)
print(nums)
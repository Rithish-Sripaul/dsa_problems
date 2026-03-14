def merge(left, mid, right, nums):
  n1 = mid - left + 1
  n2 = right - mid

  L = [0] * n1
  R = [0] * n2

  for i in range(n1):
    L[i] = nums[left + i]
  for j in range(n2):
    R[j] = nums[mid + 1 + j]
  
  i, j = 0, 0
  k = left

  while i < n1 and j < n2: 
    if L[i] <= R[j]:
      nums[k] = L[i]
      i += 1
    else:
      nums[k] = R[j]
      j += 1
    k += 1
  
  while i < n1:
    nums[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    nums[k] = R[j]
    j += 1
    k += 1


def merge_sort(left, right, nums):
  if left < right:
    mid = (left + right) // 2

    merge_sort(left, mid, nums)
    merge_sort(mid + 1, right, nums)
    merge(left, mid, right, nums)


nums = [3, 2, 1, 0, 100, 50]
merge_sort(0, len(nums) - 1, nums)
print(nums)



    
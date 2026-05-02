def merge(low, mid, high, nums):
  n1 = mid - low + 1
  n2 = high - mid

  L = [0] * n1
  R = [0] * n2

  for i in range(n1):
    L[i] = nums[low + i]
  for j in range(n2):
    R[j] = nums[mid + j + 1]

  i, j = 0, 0
  k = low

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
    k += 1
    i += 1
  
  while j < n2:
    nums[k] = R[j]
    k += 1
    j += 1

def merge_sort(low, high, nums):
  if low < high:
    mid = (low + high) // 2

    merge_sort(low, mid, nums)
    merge_sort(mid + 1, high, nums)
    merge(low, mid, high, nums)

nums = [3, 2, 1, 0, 4, 5]
merge_sort(0, len(nums) - 1, nums)
print(nums)
  

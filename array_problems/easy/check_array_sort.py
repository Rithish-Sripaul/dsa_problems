def check_array_sort(arr):
  if len(arr) <= 1:
    return True 
  for l in range(1, len(arr)):
    if arr[l - 1] > arr[l]:
      return False
  return True

arr = [1, 2, 32, 4]
print(check_array_sort(arr))
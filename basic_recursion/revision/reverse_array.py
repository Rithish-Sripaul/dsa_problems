def reverse_array(arr, n, m):
  if n >= m:
    return 
  
  arr[n], arr[m] = arr[m], arr[n]

  reverse_array(arr, n + 1, m - 1)

def reverse_array_2(arr, n, m):
  if n >= m:
    return
  
  temp = arr[m]
  arr[m] = arr[n]
  arr[n] = temp

  reverse_array_2(arr, n + 1, m - 1)

def reverse_array_3(arr, i):

  if i >= len(arr) / 2:
    return
  
  arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]

  reverse_array_3(arr, i + 1)

arr = [1, 2, 3, 4, 5]
arr = [1, 2]
reverse_array_3(arr, 0)
print(arr)
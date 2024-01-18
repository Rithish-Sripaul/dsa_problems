def left_rotate(arr):
  # first element to the last
  last = arr[0]
  for i in range(len(arr) - 1):
    arr[i] = arr[i + 1]
  arr[len(arr) - 1] = last

  return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(left_rotate(arr))
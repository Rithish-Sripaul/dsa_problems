def left_rotate_by_k(arr, k):
  for rotation in range(k):
    last = arr[0]
    for i in range(len(arr) - 1):
      arr[i] = arr[i + 1]
    arr[len(arr) - 1] = last
  return arr

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(left_rotate_by_k(arr, k))
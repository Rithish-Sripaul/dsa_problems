def rev_arr(arr, i):
  if i > len(arr) / 2:
    return arr
  arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
  return rev_arr(arr, i + 1)

arr = [1, 2, 3, 4, 7, 12]
print(rev_arr(arr, 0))
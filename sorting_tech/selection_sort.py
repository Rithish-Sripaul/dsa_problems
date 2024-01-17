def selection_sort(arr):
  l = 0
  
  while l < len(arr):
    min_ele = arr[l]
    min_ele_ind = l

    for r in range(l, len(arr)):
      if arr[r] < min_ele:
        min_ele = arr[r]
        min_ele_ind = r

    arr[l], arr[min_ele_ind] = arr[min_ele_ind], arr[l]
    l += 1
  return arr

arr = [4, 3, 2,23, 1, 10]
print(selection_sort(arr))

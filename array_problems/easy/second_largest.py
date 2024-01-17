def second_largest(arr):
  largest = arr[0]
  second_largest = arr[0]

  for i in range(len(arr)):
    if arr[i] > second_largest:
      if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
      else:
        second_largest = arr[i]
  
  return second_largest

arr = [-1, 0, 1, 2, -10, 100, 21, 101]
print(second_largest(arr))
    


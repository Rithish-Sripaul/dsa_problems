def union_of_two_sorted_array(arr1, arr2):

  i, j = 0, 0
  res = []
  while i < len(arr1) and j < len(arr2):
    while len(res) > 0 and arr1[i] == res[-1] and i < len(arr1) - 1:
      i += 1
    while len(res) > 0 and arr2[j] == res[-1] and j < len(arr2) - 1:
      j += 1
    if arr1[i] == arr2[j]:
      res.append(arr1[i])
    else:
      if arr1[i] > arr2[j]:
        res.append(arr2[j])
        
        j += 1
      else:
        res.append(arr2[i])
        i += 1
  
  return res

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]

print(union_of_two_sorted_array(arr1, arr2))
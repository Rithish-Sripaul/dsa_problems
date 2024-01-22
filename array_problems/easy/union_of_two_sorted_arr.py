def union_two_sorted_array(arr1, arr2):
  result = []
  length = max(len(arr1), len(arr2))
  a1, a2 = 0, 0
  while a1 < len(arr1) and a2 < len(arr2):
    if a1 > len(arr1):
      break
    if a2 > len(arr2):
      break

    if arr1[a1] < arr2[a2]:
      if arr1[a1] not in result:
        result.append(arr1[a1])
      a1 += 1
    elif arr2[a2] < arr1[a1]:
      if arr2[a2] not in result:
        result.append(arr2[a2])
      a2 += 1
    else:
      if arr1[a1] not in result:
        result.append(arr1[a1])
      a1 += 1
      a2 += 1
    
  while a1 < len(arr1):
    if arr1[a1] not in result:
      result.append(arr1[a1])
    a1 += 1

  while a2 < len(arr2):
    if arr2[a2] not in result:
      result.append(arr2[a2])
    a2 += 1


  return result

arr1 = [1, 2, 3, 10]
arr2 = [3, 4, 4, 5, 8, 24]
print(union_two_sorted_array(arr1, arr2))
def kth_missing(arr, k):
  low, high = 1, max(arr) + k

  while low <= high:
    middle = (low + high) // 2

    poss_pos = -1
    for i in range(len(arr)):
      if arr[i] > middle:
        if arr[0] == 1:
          poss_pos = middle - i + 1
          break
        poss_pos = middle - i
        break
      elif arr[i] == middle:
        poss_pos = middle - i
        break
      
    # It crosses the arr max
    if poss_pos == -1:
      poss_pos = (middle - arr[-1]) + (len(arr) + 1)
    if poss_pos == k:
      #print(poss_pos, middle, k)
      return middle
    elif poss_pos < k:
      low = middle + 1
    else:
      high = middle - 1
   #print(poss_pos, middle)
  return arr[-1] + k
print(kth_missing([2, 3, 4, 7, 11], 5))
print(kth_missing([1, 2, 3, 4], 2))
print(kth_missing([1, 5, 7, 10, 12], 6))
print(kth_missing([1, 2], 1))
print(kth_missing([3, 10], 2))
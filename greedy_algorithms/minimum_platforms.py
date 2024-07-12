def find(n, arr, dep):
  arr.sort()
  dep.sort()

  ans = 1
  count = 1
  i = 1
  j = 0
  while i < n and j < n:
    if arr[i] <= dep[j]:
      count += 1
      i += 1
    else:
      count -= 1
      j += 1
    ans = max(ans, count)
  return ans

      



print(find(6, [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
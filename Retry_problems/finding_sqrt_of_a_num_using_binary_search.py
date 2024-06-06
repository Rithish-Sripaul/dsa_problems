def find_sqrt(n):
  low, high = 0, n
  ans = 0
  while low <= high:
    middle = (low + high) // 2


    if middle * middle <= n:
      ans = max(middle, ans)
      low = middle + 1
    else:
      high = middle - 1
  return ans

print(find_sqrt(36))
print(find_sqrt(28))


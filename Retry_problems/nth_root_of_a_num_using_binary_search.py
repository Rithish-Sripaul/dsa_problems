def nth_root(n, m):
  low, high = 1, m

  while low <= high:
    middle = (low + high) // 2

    if middle ** n == m:
      return middle
    elif middle ** n < m:
      low = middle + 1
    else:
      high = middle - 1
  return -1
print(nth_root(3, 27))
print(nth_root(4, 69))

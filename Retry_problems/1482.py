def min_days(bloomDay, m, k):
  if m * k > len(bloomDay):
    return -1
  low, high = 1, max(bloomDay)
  ans = 0
  while low <= high:
    middle = (low + high) // 2

    b_cnt = 0
    k_crnt = 0
    for i in range(len(bloomDay)):
      if bloomDay[i] <= middle:
        k_crnt += 1
        if k_crnt == k:
          k_crnt = 0
          b_cnt += 1
      else:
        k_crnt = 0
    
    if b_cnt >= m:
      ans = middle
      high = middle - 1
    else:
      low = middle + 1
  return ans

print(min_days([1, 10, 3, 10, 2], 3, 1))
print(min_days([7, 7, 7, 7, 12, 7, 7], 2, 3))


    
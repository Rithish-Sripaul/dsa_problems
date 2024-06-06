import math
def capacity(weights, days):
  low = max(weights)
  high = math.ceil(len(weights) / days) * max(weights)
  ans = 0

  while low <= high:
    middle = (low + high) // 2
    crnt_cap = middle
    num_days = 1
    
    for weight in weights:
      if weight > crnt_cap:
        if num_days > days:
          break
        num_days += 1
        crnt_cap = middle
      crnt_cap -= weight

    if num_days <= days:
      ans = middle
      high = middle - 1
    else:
      low = middle + 1
  
  return ans

print(capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    
    
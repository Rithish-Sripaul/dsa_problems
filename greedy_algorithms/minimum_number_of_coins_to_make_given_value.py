def find(coins, v):
  coins.sort()
  i = 0
  ans = 0
  while v > 0 and i < len(coins):
    if coins[i] > v:
      i += 1
      continue
    ans += v // coins[i]
    v = v % coins[i]
  return ans

print(find([25, 10, 5], 30))
print(find([9, 6, 5, 1], 11))

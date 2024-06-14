def find(fruits):
  left = right = 0
  hash = {}
  maxLen = 0

  while right < len(fruits):
    hash[fruits[right]] = hash.get(fruits[right], 0) + 1

    while len(hash) == 3:
      hash[fruits[left]] -= 1
      if hash[fruits[left]] <= 0:
        hash.pop(fruits[left])
      left += 1
    maxLen = max(sum(hash.values()), maxLen)
    right += 1
  return maxLen
print(find([2, 1, 2]))
print(find([0,0, 1, 2, 2, 2, 2, 3, 3, 3]))
print(find([0, 1, 2, 2, 2, 2]))

      



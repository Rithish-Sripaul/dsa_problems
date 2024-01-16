hash = {}
arr = [1, 1, 2, 3, 4, 2]

for num in arr:
  if num in hash:
    hash[num] += 1
  else:
    hash[num] = 1
print(hash)

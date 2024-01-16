arr = [1, 1, 2, 2, 2, 1, 3, 3, 4, 4, 3]
hash = {}
highest = [-1, arr[0]]

for num in arr:
  if num in hash:
    hash[num] += 1
  else:
    hash[num] = 1

  if hash[num] > highest[0]:
    highest = [hash[num], num]

lowest = [len(arr), arr[0]]
for i in hash:
  if hash[i] < lowest[0]:
    lowest = [hash[i], i]

print(highest[1], lowest[1])
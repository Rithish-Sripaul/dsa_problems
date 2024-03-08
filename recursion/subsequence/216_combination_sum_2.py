def find(index, sum, path):
  if len(path) > k: return

  if len(path) == k and sum == target:
    res.append(path)
    return
  
  for i in range(index, 10):
    find(i + 1, sum + i, path + [i])

res = []
k = 3
target = 7
find(1, 0, [])
print(res)
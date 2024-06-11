def combinationSum3(index, k, n, path, s):
  if len(path) > k:
    return
   
  if len(path) == k:
    if s == n:
      res.append(path)
    return
  
  for i in range(index + 1, 10):
    combinationSum3(i, k, n, path + [i], s + i)

def combinationSum3Striver(index, k, n, path, s):
  if index == 10:
    if len(path) == k and s == n:
      print(path)
    return

  s += index
  path.append(index)

  combinationSum3Striver(index + 1, k, n, path, s)

  s -= index
  path.pop()

  combinationSum3Striver(index + 1, k, n, path, s)

res = []
combinationSum3(0, 3, 7, [], 0)
print(res)
res = []
combinationSum3(0, 3, 9, [], 0)
print(res)
res = []
combinationSum3(0, 4, 1, [], 0)
print(res)


combinationSum3Striver(1, 3, 9, [], 0)
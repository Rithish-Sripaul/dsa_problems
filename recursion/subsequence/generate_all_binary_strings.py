def dfs(ones, s):
  if len(s) == n:
    res.append(s)
    return

  if ones == 1: 
    dfs(ones - 1, s + "0")
  else: dfs(ones + 1, s + "1") or dfs(ones, s + "0")



res = []
n = 3

dfs(0, "")
print(res)
def assignCookies(g, s):
  g.sort()
  s.sort()

  i, j = 0, 0
  ans = 0
  
  while i < len(g) and j < len(s):
    if s[j] >= g[i]:
      ans += 1
      i += 1
      j += 1
    else:
      j += 1
  return ans

g = [1, 2, 3]
s = [1, 1]
print(assignCookies(g, s))

g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(assignCookies(g, s))

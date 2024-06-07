def sortChrbyFreq(s):

  hash = {}
  n = len(s)
  ans = []
  for i in s:
    hash[i] = hash.get(i, 0) + 1
  
  bucket = [[] for _ in range(n + 1)]
  for key, freq in hash.items():
    bucket[freq].append(key)
  
  for i in range(n, -1, -1):
    for c in bucket[i]:
      ans.append(c * i)
  
  return "".join(ans)

print(sortChrbyFreq("tree"))
print(sortChrbyFreq("cccaaa"))
print(sortChrbyFreq("Aabb"))
print(sortChrbyFreq("eeeee"))
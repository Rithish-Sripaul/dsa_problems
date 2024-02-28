def first_approach(s, t):

  hash_s = {}
  hash_t = {}
  hash = {}
  visited = set()
  for i in range(len(s)):
    if s[i] in hash:
      if hash[s[i]] != t[i]:
        return False
    else:
      if t[i] in visited:
        return False
      visited.add(t[i])
      hash[s[i]] = t[i]

  return True


s = "badc"
t = "baba"
print(first_approach(s, t))
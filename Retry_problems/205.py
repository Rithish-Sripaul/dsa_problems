def isomorphicStrings(s, t):
  hash = {}
  completed = []
  for i in range(len(s)):
    if s[i] not in hash:
      if t[i] in completed:
        return False
      hash[s[i]] = t[i]
      completed.append(t[i])
    else:
      if hash[s[i]] != t[i]:
        return False
  return True

print(isomorphicStrings("egg", "add"))
print(isomorphicStrings("foo", "bar"))
print(isomorphicStrings("badc", "baba"))
def find(s):
  if len(s) <= 1: return len(s)

  l, r = 0, 0
  hash = {}
  curr, ans = 0, 0
  while l <= r and r < len(s):
    while s[r] in hash and hash[s[r]] >= 1:
      hash[s[l]] -= 1
      curr -= 1
      l += 1

    hash[s[r]] = hash.get(s[r], 0) + 1
    curr += 1
    ans = max(curr, ans)

    r += 1
  return ans

hash = {}
print(find("abcabcbb"))
print(find("bbbbb"))
print(find("pwwkew"))

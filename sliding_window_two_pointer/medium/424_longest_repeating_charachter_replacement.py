def find(s, k):
  hash = {}
  left = right = 0
  maxLen = 0
  for right in range(len(s)):
    hash[s[right]] = hash.get(s[right], 0) + 1

    while (right - left + 1) - max(hash.values()) > k:
      hash[s[left]] -= 1
      left += 1

    maxLen = max(maxLen, right - left + 1)
  return max(maxLen, right - left + 1)
print(find("AABABBA", 1))
print(find("ABAB", 2))

      
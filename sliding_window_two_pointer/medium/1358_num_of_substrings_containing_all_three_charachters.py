def find(s):
  left, right = 0, 0
  hash = {}
  count = 0
  while right < len(s):
    left = right
    hash = {"a":0, "b":0, "c":0}
    while left >= 0:
      hash[s[left]] += 1
      if hash["a"] == hash['b'] == hash["c"] == 1:
        count += right - 1
        break
      left -= 1
    right += 1
  return count

def findAns(s):
  hash = {"a":-1, "b":-1, "c":-1}
  left = right = 0
  count = 0
  for right in range(len(s)):
    hash[s[right]] = right
    if -1 not in hash.values():
      left = min(hash.values())
      count += left + 1
  return count



print(findAns("abcabc"))
print(findAns("aaacb"))
print(findAns("abc"))
def longestCommonPrefix(strs):
  count = 0
  minLength = 201
  minInd = 0

  for i in range(len(strs)):
    if len(strs[i]) < minLength:
      minLength = len(strs[i])
      ind = i

  for i in range(minLength):
    start = strs[i][count]
    for j in strs:
      if j[count] != start:
        return j[:count]
    count += 1

# Sorting allowed
def sortingCommonPrefix(strs):
  strs = sorted(strs)
  ans = ""
  first, last = strs[0], strs[-1]

  for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
      return ans
    ans += first[i]
  return ans
print(sortingCommonPrefix(["flower","flow","flight"]))
print(sortingCommonPrefix(["dog","racecar","car"]))
print(sortingCommonPrefix(["a"]))
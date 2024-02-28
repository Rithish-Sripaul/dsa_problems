def first_approach(strs):
  count = 0

  min_length = 99999
  min_ele = ""
  for i in strs:
    if len(i) < min_length:
      min_length = len(i)
      min_ele = i

  for i in range(min_length):
    start = strs[0][count]
    for j in strs:
      if j[count] != start:
        print(count)
        return j[:count]
    count += 1
  
  return min_ele

def if_sorting_allowed(strs):
  ans = ""
  strs = sorted(strs)
  first = strs[0]
  last = strs[-1]

  for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
      return ans
    ans += first[i]
  return ans
strs = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
strs2 = ["ab", "a"]
strs3 = [""]

print(if_sorting_allowed(strs))
print(if_sorting_allowed(strs1))
print(if_sorting_allowed(strs2))
print(if_sorting_allowed(strs3))



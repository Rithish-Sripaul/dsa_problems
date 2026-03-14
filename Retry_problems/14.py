# Brute Force

def comparing_in_arrays(strs):

  min_length = 201

  for i in strs:
    min_length = min(len(i), min_length)

  if min_length == 0:
    return ""
  i = 0
  
  while i < min_length:
    current_prefix = ""
    for j in strs:
      if not current_prefix:
        current_prefix = j[i]
      else:
        if current_prefix != j[i]:
          return j[:i]
    i += 1
  
  return strs[0][:i]

def sorted_method(strs):
  if len(strs) == 0:
    return []
  strs = sorted(strs)
  
  length = 0
  for i in range(min(len(strs[0]), len(strs[-1]))):
    if strs[0][i] != strs[-1][i]:
      return strs[0][:length]
    length += 1
  return strs[0][:length]

strs = ["a"]
strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
print(comparing_in_arrays(strs))
print(sorted_method(strs))
        

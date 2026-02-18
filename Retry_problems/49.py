from collections import defaultdict

def groupAnagrams(strs):

  hash = defaultdict(list)

  for s in strs:
    arr = [0] * 26

    for char in s:
      arr[97 - ord(char)] += 1
    
    hash[tuple(arr)].append(s)
  
  return hash.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
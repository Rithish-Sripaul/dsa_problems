from collections import defaultdict
def groupdAnagrams(strs):
  hash = defaultdict(list)

  for s in strs:
    arr = [0] * 26

    for char in s:
      arr[ord(char) - ord("a")] += 1
    
    hash[tuple(arr)].append(s)

  return list(hash.values())

print(groupdAnagrams(["eat","tea","tan","ate","nat","bat"]))
            

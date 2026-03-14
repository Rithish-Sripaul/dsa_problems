# Group anagrams
import time
def solution(strs):
  
  hash = {}
  
  for str in strs:
    arr = [0] * 26
    for s in str:
      arr[ord(s) - 97] += 1
    arr = tuple(arr)
    if arr in hash:
      hash[arr].append(str)
    else:
      hash[arr] = [str]
  return list(hash.values())

from collections import defaultdict
def solution_defaultdict(strs):
  hash = defaultdict(list)

  for str in strs:
    arr = [0] * 26
    for s in str:
      arr[ord(s) - ord("a")] += 1
    
    hash[tuple(arr)].append(str)
  return list(hash.values())

strs = ["eat","tea","tan","ate","nat","bat"]
start_time = time.time()
print(solution(strs))
end_time = time.time()
print(f"Time taken: {end_time - start_time:.4f}")

start_time = time.time()
print(solution_defaultdict(strs))
end_time = time.time()
print(f"Time taken: {end_time - start_time:.4f}")


# O(m*n)

def first_approach(s):
  hash = {}
  visited = set()
  for i in s:
    hash[i] = hash.get(i, 0) + 1
  
  ans = []
  for i in range(len(hash)):
    max = 0
    curr_key = 0
    for key, value in hash.items():
      print(key, value)
      if value > max and key not in visited:
        max = value
        curr_key = key
    visited.add(curr_key)
    ans.append(f"{curr_key}" * max)
  return "".join(ans)


def optimal_approach(s):
  hash = {}
  n = len(s)

  for i in s:
    hash[i] = hash.get(i, 0) + 1
  
  bucket = [[] for _ in range(n + 1)]
  for key, freq in hash.items():
    bucket[freq].append(key)

  ans = []
  for freq in range(n, -1, -1):
    for c in bucket[freq]:
      ans.append(c * freq)
  
  print(bucket)
  print(ans)
  return "".join(ans)


s = "tree"
print(optimal_approach(s))
    
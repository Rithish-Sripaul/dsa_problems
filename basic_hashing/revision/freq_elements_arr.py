def solution(arr):
  

  hash = {}

  for num in arr:
    hash[num] = hash.get(num, 0) + 1

  return hash

arr = [10, 20, 10, 10, 20, 30]

print(solution(arr))
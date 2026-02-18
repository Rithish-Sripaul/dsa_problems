def solution(arr):

  highest, lowest= 0, 0

  hash = {}

  for num in arr:
    hash[num] = hash.get(num, 0) + 1

    if hash[num] > hash.get(highest, 0):
      highest = num
    elif hash[num] < hash.get(lowest, 0):
      lowest = num
  
  return [highest, lowest]


print(solution([10, 10, 10, 20, 20, 40]))

    
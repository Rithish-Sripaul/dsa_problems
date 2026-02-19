def solution(arr):
  largest = -1

  for num in arr:
    largest = num if num > largest else largest

  return largest

print(solution([10, 20, 30, 40]))
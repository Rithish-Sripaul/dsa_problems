def solution(n):
  if n < 1:
    return 0
  
  return n + solution(n - 1)

print(solution(10))
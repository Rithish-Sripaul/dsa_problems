def solution(n):
  if n < 1:
    return
  print(n)
  return solution(n - 1)

solution(10)
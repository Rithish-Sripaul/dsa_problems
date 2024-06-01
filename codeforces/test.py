for _ in range(int(input())):
  p1, p2, p3 = list(map(int, input().split()))
  sum_ = p1 + p2 + p3
  if sum_ % 2 == 1:
    print(-1)
  else:
    print(int(min(sum_/2, (p1 + p2))))
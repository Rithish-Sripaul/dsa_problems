for _ in range(int(input())):
  p1, p2, p3 = list(map(int, input().split()))
  if p1 == p2 and p2 == p3:
    if p1 == 0:
      print(0)
    else:
      print(-1)
  else:
    draws = 0
    while p1 != p2 or p2 != p3:
      if p1 > p2:
        p1, p2 = p1 - 1, p2 + 1
      elif p3 > p2:
        p3, p2 = p3 - 1, p2 + 1
      else:
        p2, p3 = p2 - 1, p3 + 1
      draws += 1
    print(draws)
    draws = 0
    arr = [p1, p2, p3]
    arr.sort(reverse=True)
    while arr[1] != 0:
      draws += arr[1]
      arr[0] -= arr[1]
      arr[1] = 0
      arr.sort(reverse = True)

    #print(draws)
    draws = 0
    draws = p2
    p3 -= p2
    p2 = 0

    if p3 == 0 and p1 % 2 == 1:
      print(-1)
    else:
      if p3 < p1:
        draws += p3 + 1
      else:
        draws += p1
    #print(draws)
 

def find(Jobs, n):
  Jobs.sort(key= lambda x: x[2], reverse=True)
  maxDeadline = 0
  for _ in range(n):
    maxDeadline = max(maxDeadline, Jobs[_][1])
  
  slot = [-1] * (maxDeadline + 1)
  ans = [0, 0]
  for i in range(n):
    for j in range(Jobs[i][1], 0, -1):
      if slot[j] == -1:
        slot[j] = Jobs[i][0]
        ans[0] += 1
        ans[1] += Jobs[i][2]
        break
  return ans

  print(slot)


print(find([(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)], 5))
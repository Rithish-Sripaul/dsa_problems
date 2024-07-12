def find(n, start, end):
  meet = [[start[i], end[i], i + 1] for i in range(n)]
  meet.sort(key= lambda x: (x[1], x[2]))

  ans = 0
  lastEnd = 0
  for m in meet:
    if m[0] > lastEnd:
      ans += 1
      lastEnd = m[1]
  return ans
  print(meet)

print(find(6, [1, 0, 3, 8, 5, 8], [2, 6, 4, 9, 7, 9]))
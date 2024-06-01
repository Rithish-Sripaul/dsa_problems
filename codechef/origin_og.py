def getOrigin(previousOrigin, n):
  if n <= 1:
    return previousOrigin +1
  return getOrigin(previousOrigin + (n % 10), n // 10)

for _ in range(int(input())):
  n = int(input())
  count = 0
  for i in range(n):
    count += getOrigin(0, i)
  print(count)
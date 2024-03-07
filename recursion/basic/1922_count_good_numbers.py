def rec(n):
  if n == 1: return 5 
  if n % 2 == 0: return (4 * rec(n - 1)) % ((10**9) + 7)
  return (5 * rec(n - 1)) % ((10**9) + 7)

def pow(x, n, m):
  if n == 0: return 1

  temp = pow(x, n // 2, m)
  if (n % 2 == 0): return (temp * temp) % m
  return (x * temp * temp) % m
n = 50
m = (10**9) + 7
even = (n + 1) / 2
odd = n / 2
first = pow(5, even, m) % m
second = pow(4, odd, m) % m

print((first * second) % m)


# print(rec(4))
# print(rec(50))
# print(rec_optimal(20, 50, (10**9) + 7))


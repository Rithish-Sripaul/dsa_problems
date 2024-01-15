# 1, 1, 2, 3, 5, 8, ...

def fibo_num(a, b, n):
  if n == 0:
    return 0
  if n <= 2:
    return a + b
  # c = a + b
  return fibo_num(b, a + b, n - 1)
print(fibo_num(0, 1, 4))

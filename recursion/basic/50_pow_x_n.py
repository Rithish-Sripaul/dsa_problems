
def pow(x, n ):
  if n == 0:
    return 1
  elif n % 2 == 0:
    return pow(x * x, n // 2)
  else:
    return x * pow(x * x, (n-1) // 2)

x = 0.00001
y = 2147483647

print(pow(x, y))
# print(pow(2, -2))




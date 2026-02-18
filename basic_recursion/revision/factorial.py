def find_factorial(n):
  if n == 0:
    return 1
  
  return n * find_factorial(n - 1)

print(find_factorial(0))
print(find_factorial(1))
print(find_factorial(2))
print(find_factorial(3))
print(find_factorial(4))

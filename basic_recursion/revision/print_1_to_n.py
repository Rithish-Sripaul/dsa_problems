def print_1_to_n(n, m):
  if m > n:
    return 
  print(m)
  return print_1_to_n(n, m + 1)
print_1_to_n(10, 1)
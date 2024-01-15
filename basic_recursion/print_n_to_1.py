def print_n_to_1(n):
  if n < 1:
    return
  print(n)
  return print_n_to_1(n - 1)

print_n_to_1(10)
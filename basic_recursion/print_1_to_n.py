def print_1_to_n(n, count):
  if count > n:
    return
  print(count)
  return print_1_to_n(n, count + 1)

print_1_to_n(5, 1)
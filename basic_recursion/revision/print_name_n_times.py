def print_name_n_times(name, n):
  if n == 0:
    return
  print(name)
  return print_name_n_times(name, n - 1)

print_name_n_times("Testing", 5)
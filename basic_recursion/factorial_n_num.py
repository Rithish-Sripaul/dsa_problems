def fact_n_num(n):
  if n == 1:
    return 1
  return n * fact_n_num(n - 1)

print(fact_n_num(5))
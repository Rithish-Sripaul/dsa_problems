def first_approach(x, n):
	if n == 0: return 1
	return x * first_approach(x, n - 1)

print(first_approach(2, 10))
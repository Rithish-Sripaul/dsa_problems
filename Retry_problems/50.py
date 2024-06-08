def pow(x, n):
	if n == 0: return 1

	if n < 0: return (1/x) * pow(x, n + 1)
	return x * pow(x, n - 1)

print(pow(2, 10))
print(pow(2.1, 3))
print(pow(2, -2))
# Count good Number

def first_approach(ans, n, mod):
	if n == 1: return (ans * 5) % mod

	if n % 2 == 1: return first_approach((20 * ans* 5)  % mod, n // 2, mod)
	return first_approach((20 * ans) % mod, n // 2, mod)

mod = (10**9) + 7
print(first_approach(1, 50, mod))

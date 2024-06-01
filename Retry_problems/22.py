def generate(left, right, n, s):
	if len(s) == n*2:

		res.append(s)
		return 

	if left < n:
		generate(left + 1, right, n, s + "(")
	if right < left:
		generate(left, right + 1, n, s + ")")




res = []
n = 3
generate(0, 0, n, "")
print(res)



	
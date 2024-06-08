def generateParantheses(left, right, s):
	if len(s) == 2 * n:
		res.append(s)
		return


	if left < n:
		generateParantheses(left + 1, right, s + "(")
	if right < left:
		generateParantheses(left, right + 1, s + ")")
		

	 

res = []
n = 3
generateParantheses(0, .0, "")
print(res)

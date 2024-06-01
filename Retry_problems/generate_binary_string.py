def binary_string(ones, s):
	if len(s) == n:
		res.append(s)
		return

	if ones == 1:
		binary_string(ones - 1, s + "0")
	else:
		binary_string(ones + 1, s + "1") or binary_string(ones, s + "0")
	
		
	
	



res = []
n = 3
binary_string(0, "")
print(res)

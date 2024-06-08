def generateBinaryStrings(ones, s):
	if len(s) == n:
		res.append(s)
		return

	if ones == 1:
		generateBinaryStrings(ones - 1, s + "0")
	else:
		generateBinaryStrings(ones + 1, s + "1") or generateBinaryStrings(ones, s + "0")

def binaryStrings2(zeros, s):
	if len(s) == n:
		res.append(s)
		return

	if zeros == 1:
		binaryStrings2(zeros - 1, s + "1")
	else:
		binaryStrings2(zeros + 1, s + "0") or binaryStrings2(zeros, s + "1")



res = []
n = 4
binaryStrings2(0, "")
print(res)
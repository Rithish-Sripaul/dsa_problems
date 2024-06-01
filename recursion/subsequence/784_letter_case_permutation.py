def find(index, path):
	
	if len(path) == len(s):
		res.append(path)
		return
	if index == len(s):
		return 
	
	if s[index].isalpha():
		find(index + 1, path + s[index].upper())
		find(index + 1, path + s[index].lower())
	else:
		find(index + 1, path + s[index])

s = "a1b2"
res = []
find(0, "")
print(res)


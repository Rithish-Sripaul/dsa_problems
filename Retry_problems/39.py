def combinationSum(index, s, path):
	if index == len(candidates) or s > target:
		if s == target:
			res.append(path)
		return
	
	if s == target:
		res.append(path)
	for i in range(index, len(candidates)):
		combinationSum(i, s +  candidates[i], path + [candidates[i]])

def combinationSumStriver(index, s, path):
	if index == len(candidates) or s > target:
		if s == target:
			ans = []
			for i in path: ans.append(i)
			res.append(ans)
		return
	
	s += candidates[index]
	path.append(candidates[index])
 
	combinationSumStriver(index, s, path)

	s -= candidates[index]
	path.pop()
	combinationSumStriver(index + 1, s, path)

candidates = [2, 3, 6, 7]
target = 7
res = []
combinationSumStriver(0, 0, [])
print(res)

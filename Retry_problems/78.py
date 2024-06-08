def subsets(index, path):

	if len(path) == len(nums):
		res.append(path)
		return
	res.append(path)
	for i in range(index, len(nums)):
		subsets(i + 1, path + [nums[i]])
	


res = []
nums = [1, 2, 3]
subsets(0, [])
print(sorted(res))
	

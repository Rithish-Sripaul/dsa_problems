# 78 Subsets

def find(i, path):
	if len(res) == 2 ** len(nums): return

	if len(path) == len(nums):
		res.append(path)
		return

	res.append(path)
	for j in range(i, len(nums)):
		find(j + 1, path + [nums[j]])

res = []
nums = [1, 2, 3]
find(0, [])
print(res)

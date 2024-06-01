def find(index, sum_, path):
	if sum_ > target:
		return

	if sum_ == target:
		res.append(path)
		return

	for i in range(len(candidates)):
		find(i + 1, sum_ + candidates[i], path + [candidates[i]])

candidates = [2, 3, 6, 7]
target = 7
res = []
find(0, 0, [])
print(res)

def solutions(grid):

	count = 0
	rows = len(grid)
	if not rows: return 0
	cols = len(grid[0])

	def dfs(i, j):
		if i < 0 or i == rows or j < 0 or j == cols: return
		if grid[i][j] != "1": return

		grid[i][j] = "#"
		dfs(i + 1, j)
		dfs(i - 1, j)
		dfs(i, j + 1)
		dfs(i, j - 1)

	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == "1":
				dfs(i, j)
				count += 1

	
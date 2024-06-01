from collections import deque
def solutions(grid):

	rows = len(grid)
	if not row: return []
	cols = len(grid[0])
	visiter = set()
	q = deque()
	count = 0

	for i in range(rows):
		for j in range(cols):
			if i == rows - 1 or j == cols - 1 or i == 0 or j == 0:
				if grid[i][j] == 1:
					q.append((i, j))
					visited.add((i, j))
					count += 1

	if count == 0: return 0

	while q:
		x, y = q.popleft()

		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			xx, yy = x + dx, y + dy

			if xx < 0 or x == rows or y < 0 or y == cols:
				continue

			if grid[xx][yy] == 0 or (xx, yy) in visited:
				continue

			visited.add((xx, yy))
			q.append((xx, yy))
			count += 1

	return count


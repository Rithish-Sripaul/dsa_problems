from collections import deque
def solution(grid):

	rows = len(grid)
	if not rows: return 0

	cols = len(grid[0])

	fresh_oranges = 0
	rotten = deque()
	minutes_passed = 0

	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == 2:
				rotten.append((i, j))
			else:
				fresh_oranges += 1

	while rotten and fresh_oranges > 0:
		minutes_passed += 1

		for _ in range(len(rotten)):
			x, y = rotten.popleft()

			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				xx, yy = x + dx, y + dy

				if xx < 0 or xx == rows or yy < 0 or yy == cols:
					continue

				if grid[xx][yy] == 0 or grid[xx][yy] == 2:
					continue

				fresh_cnt -= 1
				grid[xx][yy] = 2
				rotten.append((xx, yy))

	return minutes_passed if fresh_cnt == 0 else -1




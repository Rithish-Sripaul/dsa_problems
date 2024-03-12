from collections import deque
def solution(mat):
	visited = set()
	rows, cols = len(mat), len(mat[0])
	q = deque()

	for i in range(rows):
		for j in range(cols):
			if mat[i][j] == 0:
				q.append((i, j))
				visited.add((i, j))
	dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	while q:
		x, y = q.popleft()
		for dx, dy in dirs:
			xx, yy = dx + x, dy + y

			if xx < 0 or xx == rows or yy < 0 or yy == cols:
				continue

			if (xx, yy) in visited:
				continue

			matrix[xx][yy] = matrix[x][y] + 1
			visited.add((xx, yy))
			q.append((xx, yy))


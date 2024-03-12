from collections import deque
def solution(board):
	rows = len(board)
	if rows == 0: return []

	cols = len(board[0])

	safe = set()
	q = deque()
	for i in range(rows):
		for j in range(cols):
			if i == rows - 1 or j == cols - 1:
				if board[i][j]:
					q.append((i, j))

	while q:
		x, y = q.popleft()

		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			xx, yy = x + dx, y + dy

			if xx < 0 or xx == rows or yy < 0 or yy == cols:
				continue

			if board[xx][yy] == "X":
				continue

			safe.append((xx, yy))
			q.append((xx, yy))

	for i in range(rows):
		for j in range(cols):
			if board[i][j] == "O" and (i, j) not in safe:
				board[i][j] = "X"

	return board
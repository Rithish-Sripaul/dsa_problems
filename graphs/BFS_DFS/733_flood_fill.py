from collections import deque
def solution(image, sr, sc, color):

	rows = len(image)
	if not rows: return []

	cols = len(image[0])

	q = deque((sr, sc))

	while q:
		for _ in range(len(q)):
			x, y = q.popleft()

			for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				xx, yy = dx + x, y + dy

				if xx < 0 or xx == rows or yy < 0 or yy == cols:
					continue

				if image[xx][yy] == 0 or image[xx][yy] == 2:
					continue

				image[xx][yy] = 2
				q.append((xx, yy))
	return image
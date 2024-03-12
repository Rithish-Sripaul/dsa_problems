def solution(M):

	n = len(M)
	vis = [False] * n
	count = 0

	def dfs(u):
		for v in range(n):
			if M[u][v] == 1 and not vis[v]:
				vis[v] = True
				dfs(v)

	for i in range(n):
		if not vis[i]:
			vis[i] = True
			dfs(i)
			count += 1
	return count
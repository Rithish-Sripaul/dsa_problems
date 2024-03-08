def bfs_approach(root):

	if not root: return 0

	Q = [root]
	temp = []
	count = 0

	while Q:

		node = Q.pop(0)

		if node.left: temp.append(node.left)
		if node.right: temp.append(node.right)

		if not Q:
			count += 1
			Q = temp
			temp = []

	return count

def dfs_approach(root, level):

	if not root: return level 

	return max(dfs_approach(root.left, level + 1), dfs_approach(root.right, level + 1))
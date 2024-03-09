# METHOD 1: (OPTIMISED) Based on DFS
def check(root):
	if root is None: return 0

	left = check(root.left)
	right = check(root.right)

	if left == -1 or right == -1 or abs(left - right) > 1:
		return -1
	return 1 + max(left, right)

	return check(left, right) != -1

# METHOD 2: (Slower O(N^2))
def depth(root):
	if root is None: return 0
	return max(depth(root.left), depth(root.right)) + 1

def isBalanced(root):
	if not root: return True

	left = depth(root.left)
	right = depth(root.right)

	return abs(left - right) <= 1 and isBalanced(root.left) and isBalanced(root.right)

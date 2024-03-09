class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def builTree(nums):
	if not nums: return None

	root = TreeNode(nums[0])
	q = [root]
	i = 1

	while i < len(nums):
		curr = q.pop(0)
		if i < len(nums):
			curr.left = TreeNode(nums[i])
			q.append(curr.left)
			i += 1

		if i < len(nums):
			curr.right = TreeNode(nums[i])
			q.append(curr.right)
			i += 1
	return root

max_path = float("-inf")
def get_max_gain(node):
	notlocal max_path
	if node is None: return 0

	gain_on_left = max(get_max_gain(node.left), 0)
	gain_on_right = max(get_max_gain(node.right), 0)

	current_max_path = node.val + gain_on_left + gain_on_right
	max_path = max(max_path, current_max_path)

	return node.val + max(gain_on_left, gain_on_right)
  

maxValue = -3010
nums = [1, 2, 3]
nums = [-10,9,20,None,None,15,7]
root = builTree(nums)
print(dfs(root, maxValue))
print(maxValue)
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class binaryTree:
	def __init__(self):
		self.root = None
		self.count = 0

	def buildTree(self, nums):
		if not nums: return

		self.root = Node(nums[0])
		q = [self.root]
		i = 1

		while i < len(nums):
			node = q.pop(0)

			if i < len(nums):
				if nums[i] is not None:
					node.left = Node(nums[i])
					q.append(node.left)
				i += 1
			else:
				if nums[i] is not None:
					node.right = Node(nums[i])
					q.append(node.right)
				i += 1
		return self.root

	def search(self, root, k):
		if root:
			self.search(root.left, k)
			if self.count == k - 1:
				return root.val
			self.count += 1
			self.search(root.right, k)


nums = [3, 1, 4, None, 2]
k = 1
tree = binaryTree()
tree.buildTree(nums)
tree.search(tree.root, k)
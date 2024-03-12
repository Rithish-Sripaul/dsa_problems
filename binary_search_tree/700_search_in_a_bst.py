class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class binaryTree:
	def __init__(self):
		self.root = None

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

	def search(self, root, target):
		if root:
			if target == root.val:
				print("FOUND")
				return root
			if target < root.val:
				return self.search(root.left, target)
			return self.search(root.right, target)


nums = [4, 2, 7, 1, 3]
target = 2
tree = binaryTree()
tree.buildTree(nums)
tree.search(tree.root, target)
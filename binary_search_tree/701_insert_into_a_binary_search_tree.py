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
			if i < len(nums):
				if nums[i] is not None:
					node.right = Node(nums[i])
					q.append(node.right)
				i += 1
		return self.root

	def insert(self, root, val):
		if root.val < val:
			if not root.right:
				root.right = Node(val)
				return
			self.insert(root.right, val)
		elif root.val > val:
			if not root.left:
				root.left = Node(val)
				return
			self.insert(root.left, val)

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print(root.val, end = " ")
			self.inorder(root.right)


nums = [4, 2, 7, 1, 3]
val = 5
tree = binaryTree()
tree.buildTree(nums)
tree.inorder(tree.root)
print()
tree.insert(tree.root, val)
tree.inorder(tree.root)

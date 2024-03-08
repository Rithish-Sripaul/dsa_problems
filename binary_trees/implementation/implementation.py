class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class BinaryTree:
  def __init__(self, data):
    self.root = Node(data)
  
  def insert(self, data):
    node = Node(data)

    if self.root is None:
      self.root = node
      return

    queue = [self.root]
    while queue:
      currNode = queue.pop(0)
      if currNode.left is None:
        currNode.left = node
        break
      else:
        queue.append(currNode.left)
      if currNode.right is None:
        currNode.right = node
        break
      else:
        queue.append(currNode.right)

  def printInorder(self, root):
    if root:
      self.printInorder(root.left)
      print(root.data, end = " ")
      self.printInorder(root.right)

  def inorder(self):
    self.printInorder(self.root)
    print()
  
  def printPreorder(self, root):
    if root:
      print(root.data, end = " ")
      self.printPreorder(root.left)
      self.printPreorder(root.right)
    
  def preOrder(self):
    self.printPreorder(self.root)
    print()

  def printPostorder(self, root):
    if root:
      self.printPostorder(root.left)
      self.printPostorder(root.right)
      print(root.data, end= " ")
    
  def postOrder(self):
    self.printPostorder(self.root)
    print()

tree = BinaryTree(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.inorder()
tree.preOrder()
tree.postOrder()
def traverse(root):
  if root:
    print(root.val)
    traverse(root.left)
    traverse(root.right)104
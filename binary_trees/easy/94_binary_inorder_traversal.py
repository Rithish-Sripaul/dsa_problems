def traverse(root):
  if root:
    traverse(root.left)
    ans.append(root.val)
    traverse(root.right)

ans = []
traverse(root)

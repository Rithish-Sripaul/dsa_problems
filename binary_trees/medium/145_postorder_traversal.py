def traverse(root):
  if root:
    traverse(root.left)
    traverse(root.right)
    ans.append(root.val)

ans = []
traverse(root)
return ans
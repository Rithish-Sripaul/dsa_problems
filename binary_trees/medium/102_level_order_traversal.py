def printLevelOrder(root):
  if not root: return root

  Q = [root]
  levels = [[root.val]]
  temp = []

  while Q:
    node = Q.pop(0)

    if node.left: temp.append(node.left)
    if node.right: temp.append(node.right)

    if not Q:
      if temp:
        levels.append([n.val for n in temp])
      Q = temp
      temp = []
  return levels


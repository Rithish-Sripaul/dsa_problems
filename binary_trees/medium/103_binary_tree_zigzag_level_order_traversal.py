def traverse(root):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    q = [root]
    temp = []
    lvls = [[root.val]]
    normalOrder = False
    while q:
      node = q.pop(0)

      if node.left: temp.append(node.left)
      if node.right: temp.append(node.right)

      if not q:
        if temp:
          if normalOrder:
            lvls.append([i.val for i in temp])
          else:
            lvls.append([i.val for i in temp[::-1]])
        q = temp
        temp = []  
        normalOrder = not normalOrder
    return lvls
	


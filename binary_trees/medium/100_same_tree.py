def same_tree(p, q):
	# If both p and q are null, return True
	if not q and not p:
		return True
	# If one of P and Q are null, return False
	if not q or not p:
		return False

	if p.val == q.val:
		return same_tree(p.left, q.left) and same_tree(p.right, q.right)
	return False

	

	
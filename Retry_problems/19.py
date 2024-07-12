def removeNthNodeFromEndOfList(head, n):

  if not head: return None

  slow, fast = slow.next, fast.next

  for _ in range(n): fast = fast.next

  if not fast: return head.next
  while fast.next: slow, fast = slow.next, fast.next

  slow.next = slow.next.next
  return head 
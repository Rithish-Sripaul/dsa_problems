def reverseLL(head):
  current = head
  prev = None

  while current:
    next = current.next
    current.next = prev
    prev = current
    curretn = None

  head = prev
  return head
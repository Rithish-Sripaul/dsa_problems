def reverse_linked_list(head):
  prev = None
  current = head

  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  head = prev
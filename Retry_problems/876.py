def middleOfLinkedList(head):
  slow, fast = head, head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  
  return slow
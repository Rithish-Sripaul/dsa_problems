def first_approach(head):

  slow, fast = head, head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  
  return slow

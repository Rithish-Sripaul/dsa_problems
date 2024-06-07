def linkedListCycle2(head):
  slow, fast = head, head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

    if slow == fast:
      slow = head
      while slow != fast:
        slow, fast = slow.next, fast.next
      return slow
  
  return slow
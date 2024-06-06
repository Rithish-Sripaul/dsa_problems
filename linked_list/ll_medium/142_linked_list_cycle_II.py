def first_approach(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      slow = head
      while slow != fast:
        slow, fast = slow.next, fast.next

      return slow
    
  return None
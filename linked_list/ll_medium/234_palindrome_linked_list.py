def first_approach(head):

  slow, fast = head, head
  count = 0
  while fast and fast.next:
    count += slow.val
    slow = slow.next
    fast = fast.next.next
  
  while slow:
    count -= slow.val
    slow = slow.next
  
  if not count:
    return True
  return False
  
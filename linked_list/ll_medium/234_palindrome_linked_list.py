def stack_approach(head):

  slow, fast = head, head
  if not slow.next:
    return True
  stack = []

  while fast and fast.next:
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next
  
  if fast and not fast.next and slow.next:
    slow = slow.next
  while slow:
    if slow.val != stack[-1]:
      return False
    slow = slow.next
    stack.pop()
  
  return True
  
def reversal_approach(head):
  slow, fast = head, head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  prev = slow
  slow = slow.next
  prev.next = None
  while slow:
    next = slow.next
    slow.next = prev
    prev = slow
    slow = next

  fast, slow = head, prev
  while slow:
    if fast.val != slow.val: return False
    fast, slow = fast.next, slow.next
  return True

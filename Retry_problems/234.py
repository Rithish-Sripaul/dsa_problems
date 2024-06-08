def palindromeLL(head):
  slow, fast = head, head
  while fast and fast.next:
    slow, fast = slow.next, fast.next.next
      
      # Reversing the second half
  current = slow
  prev = None
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  secondHead = prev     
  while head and secondHead:
    if head.val != secondHead.val:
      return False
    head, secondHead = head.next, secondHead.next
  return True
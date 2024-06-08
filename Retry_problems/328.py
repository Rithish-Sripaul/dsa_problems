def oddEvenLL(head):
  if head is None:
    return None

  odd, even = head, head.next
  eHead = even

  while even and even.next:
    odd.next = even.next
    even.next = even.next.next
    odd = odd.next
    even = even.next

  odd.next = eHead
  return head  
  

def first_approach(head):
  if not head: return head

  odd = head
  even = head.next
  eHead = even

  while even and even.next:
    odd.next = even.next
    even = odd.next
    even.next = odd.next
    even = even.next
  odd.next = eHead
  return head

  

    


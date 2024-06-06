def first_approach(head, n):

  if not head: return head

  slow, fast = head, head.next
  temp = head
  c = 0
  while temp:
    c+=1
    temp = temp.next

  if c == n:
    head = head.next
    return head
  
  for i in range(c - n - 1):
    slow = slow.next
    fast = fast.next

  if not fast:
    slow.next = None
  else: 
    slow.next = fast.next

  return head 

def optimal_approach(head, n):
  if not head: return head

  slow, fast = head, head
  
  for _ in range(n): fast = fast.next
  if not fast: return head.next
  while fast.next: slow, fast = slow.next, fast.next

  slow.next = slow.next.next
  return head

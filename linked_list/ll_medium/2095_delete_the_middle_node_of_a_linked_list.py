def first_approach(head):

  prev, slow, fast = head, head, head

  while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next
  if slow == fast:
    return head.next
  prev.next = slow.next
  return head

def optimal_approach(head):
  if not head.next: return None
  slow, fast = head, head.next.next

  while fast and fast.next: slow, fast = slow.next, fast.next.next

  slow.next = slow.next.next
  return head
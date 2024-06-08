def intersectionOfTwoLinkedList(headA, headB):
  lenA, lenB = 0, 0
  tempA, tempB = headA, headB

  while tempA:
    lenA += 1
    tempA = tempA.next
  
  while tempB:
    lenB += 1
    tempB = tempB.next

  if tempA > tempB:
    count = tempA - tempB
    for _ in range(count):
      headA = headA.next
  else:
    count = tempB - tempA
    for _ in range(count):
      headB = headB.next
  
  while headA and headB:
    if headA == headB:
      return headA
    headA, headB = headA.next, headB.next
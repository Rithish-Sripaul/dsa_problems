def first_approach(headA, headB):

  tempA, tempB = headA, headB
  countA, countB = 0, 0

  while tempA: countA, tempA = countA + 1, tempA.next
  while tempB: countB, tempB = countB + 1, tempB.next

  min_count = min(countA, countB)
  if countA < countB:
    for _ in range(countB - countA):
      headB = headB.next
  else:
    for _ in range(countA - countB):
      headA = headA.next

    while headA and headB:
      if headA == headB: return headA
      headA, headB = headA.next, headB.next
    
    return None
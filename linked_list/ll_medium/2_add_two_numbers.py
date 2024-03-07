def first_approach(l1, l2):

  temp1, temp2 = l1, l2
    bigLL, smallLL = None, None
    ans = ListNode(0)
    tail = ans
    while temp1 and temp2: temp1, temp2 = temp1.next, temp2.next

    if temp1: bigLL, smallLL = l1, l2
    else: bigLL, smallLL = l2, l1

    carry = 0

    while smallLL:
      sum_ = (bigLL.val + smallLL.val + carry) 
      tail.next = ListNode(sum_ % 10)
      tail = tail.next
      carry = sum_ // 10
      smallLL, bigLL = smallLL.next, bigLL.next
    
    while bigLL:
      sum_ = bigLL.val + carry
      tail.next = ListNode(sum_%10)
      tail = tail.next
      carry = sum_ // 10
      bigLL = bigLL.next
    if carry: tail.next = ListNode(carry)
    return ans.next

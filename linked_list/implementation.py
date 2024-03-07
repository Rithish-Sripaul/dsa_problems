class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, head=None):
    self.head = head
    self.tail = None

  def append(self, value):
    newNode = Node(value)
    current = self.head
    if current:
      while current.next:
        current = current.next
      current.next = newNode
      self.tail = current.next
    else:
      self.head = newNode
      self.tail = self.head

  def display(self):
    current = self.head
    if current:
      while current:
        print(current.value)
        current = current.next

    else:
      print("Empty Linked List")

  def get_head(self):
    print(f"Head: {self.head.value}")

  def get_tail(self):
    print(f"Tail: {self.tail.value}")

  def seggregatedEvenOdd(self):
    if self.head is None:
      print("The linked list is empty")

    evenHead, evenTail = None, None
    oddHead, oddTail = None, None

    current = self.head
    while current:
      if current.value % 2 == 0:
        if evenHead is None:
          evenHead, evenTail = current, current
        else:
          evenTail.next = current
          evenTail = current
      else:
        if oddHead is None:
          oddHead, oddTail = current, current
        else:
          oddTail.next = current
          oddTail = current
      current = current.next

    if evenHead is not None:
      evenTail.next = oddHead

    if oddHead is not None:
      oddTail.next = None
    
    if evenHead is not None:
      self.head = evenHead
    else:
      self.head = oddHead
    
list1 = LinkedList()
list1.append(23)
list1.append(24)
list1.append(25)
list1.append(26)

list1.display()
list1.get_head()
list1.get_tail()

list1.seggregatedEvenOdd()
list1.display()
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    

def delete_tail(head):

  if head is None or head.next is None:
    return None
  
  temp = head

  while temp.next.next is not None:
    temp = temp.next

  temp.next = None

  return head

if __name__ == "__main__":
  arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
  head = Node(arr[0])
  head.next = Node(arr[1])
  head.next.next = Node(arr[2])
  head.next.next.next = Node(arr[3])
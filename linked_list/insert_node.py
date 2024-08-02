# O(index) / O(1)

def insert_node(head, value, index):

  dummy = Node(0)
  dummy.next = head
  prev = dummy

  while index:
    prev = head
    head = head.next
    index -= 1

  new_node = Node(value)
  old_next = prev.next
  prev.next = new_node
  new_node.next = old_next

  return dummy.next
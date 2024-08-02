# O(n) / O(n) 

def create_linked_list(values):

  if not values: return None
    
  dummy = Node(0)
  tail = dummy

  for char in values:
    tail.next = Node(char)
    tail = tail.next

  return dummy.next
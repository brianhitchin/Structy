# O(n) / O(1)

def remove_node(head, target_val):

  # Takes care of the edge case where the head == value
  if head.val == target_val:
    next = head.next
    head.next = None
    return next
  
  prev = None
  traveler = head
  
  while traveler:

    if traveler.val == target_val:
      prev.next = traveler.next
      break

    prev = traveler
    traveler = traveler.next

  return head
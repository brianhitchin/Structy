# Cool trick to merge, using dummy + tail
# O(n or m) - whichever is shorter, O(n + m)

def zipper_lists(head_1, head_2):

  dummy = Node(0)
  tail = dummy
  
  while head_1 and head_2:

    tail.next = head_1
    head_1 = head_1.next
    tail = tail.next

    tail.next = head_2
    head_2 = head_2.next
    tail = tail.next

  if head_1:
    tail.next = head_1
  
  elif head_2:
    tail.next = head_2

  return dummy.next 
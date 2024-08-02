# Very similar to zipper_list, but value comparison 
# O(n or m) - whichever is shorter, O(n + m)

def merge_lists(head_1, head_2):
  
  dummy = Node(0)
  tail = dummy
  
  while head_1 and head_2:

    if head_1.val >= head_2.val:
      tail.next = head_2
      head_2 = head_2.next
      tail = tail.next
    else:
      tail.next = head_1
      head_1 = head_1.next
      tail = tail.next

  if head_1:
    tail.next = head_1
  
  elif head_2:
    tail.next = head_2

  return dummy.next
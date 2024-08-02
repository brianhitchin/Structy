# O(n) / O(1)

def is_univalue_list(head):
  
  prev = None

  while head:
    if prev == None:
      prev = head.val
    if head.val != prev:
      return False
    head = head.next

  return True

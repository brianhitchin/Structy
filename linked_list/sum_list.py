# O(n) / O(1)

def sum_list(head):
  
  val = 0

  while head:
    val += head.val
    head = head.next

  return val

# O(n) / O(1)

def reverse_list(head):

  th = head
  prev = None
  
  while th:

    nxt = th.next
    th.next = prev
    prev = th
    th = nxt

  return prev
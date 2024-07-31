# O(n) / O(1)

def get_node_value(head, index):

  while head:

    if index == 0:
      return head.val

    head = head.next
    index -= 1

  return None
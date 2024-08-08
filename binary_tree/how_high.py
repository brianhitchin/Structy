# O(n) / O(n)

def how_high(node):

  if not node: return -1

  return 1 + max(how_high(node.left), how_high(node.right))
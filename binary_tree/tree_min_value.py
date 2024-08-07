# O(n) / O(n)

def tree_min_value(root):

  if not root: return float('inf')
  return min(root.val, tree_min_value(root.left), tree_min_value(root.right))
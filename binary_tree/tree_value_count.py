# O(n) / O(n)

def tree_value_count(root, target):

  if not root:
    return 0

  found = False
  if root.val == target:
    found = True
     
  left_count = tree_value_count(root.left, target)
  right_count = tree_value_count(root.right, target)

  return left_count + right_count + 1 if found else left_count + right_count
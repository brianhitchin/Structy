# O(n) / O(n)

def max_path_sum(root):

  # Do not traverse down this path, neg. inf. as we are looking for a max sum
  if not root: return float('-inf')
  if not root.left and not root.right: return root.val
    
  left = max_path_sum(root.left)
  right = max_path_sum(root.right)
  
  return max(left, right) + root.val

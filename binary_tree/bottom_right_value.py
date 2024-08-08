# O(n) / O(n)
# BFS - last value standing is the right most

import collections

def bottom_right_value(root):

  if not root: return root

  q = collections.deque([root])
  last = None
  
  while q:
    
    n = q.popleft()
    if n:
      last = n.val
      q.append(n.left)
      q.append(n.right)

  return last
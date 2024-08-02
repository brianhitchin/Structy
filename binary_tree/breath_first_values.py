# O(n) / O(n)

import collections

def breadth_first_values(root):

  if not root: return []
  
  q = collections.deque([root])
  res = []
  
  while q:

    n = q.popleft()
    res.append(n.val)
    if n.left:
      q.append(n.left)
    if n.right:
      q.append(n.right)

  return res
# O(n) / O(n)

import collections

def level_averages(root):

  if not root: return []
  
  q = collections.deque([root])
  res = []
  
  while q:

    inter = 0
    l = len(q)
  
    for i in range(l):
      n = q.popleft()
      inter += n.val
      if n.left: q.append(n.left)
      if n.right: q.append(n.right)

    res.append(inter / l)
    inter = 0

  return res
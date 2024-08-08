import collections

def tree_levels(root):

  if not root: return []
  
  q = collections.deque([root])
  res = []
  
  while q:

    inter = []
    l = len(q)
  
    for i in range(l):
      n = q.popleft()
      inter.append(n.val)
      if n.left: q.append(n.left)
      if n.right: q.append(n.right)

    res.append(inter)
    inter = []

  return res
# O(V + E) / O(V)

import collections

def shortest_path(edges, node_A, node_B):

  visited = set()
  
  adj = {}
  
  for nA, nB in edges:
    if nA not in adj:
      adj[nA] = []
    if nB not in adj:
      adj[nB] = []
    adj[nA].append(nB)
    adj[nB].append(nA)

  q = collections.deque([[node_A, 0]])
  visited = set([node_A])

  while q:
    
    node, d = q.popleft()
    if node == node_B:
      return d
    visited.add(node)
    for n in adj[node]:
      if n not in visited:
        q.append([n, d + 1])
  
  return -1
  
    
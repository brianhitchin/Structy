# O(V + E) / O(V + E)

import collections

def undirected_path(edges, node_A, node_B):

  adj = {}
  for a, b in edges:
    if a not in adj:
      adj[a] = []
    if b not in adj:
      adj[b] = []
    adj[a].append(b)
    adj[b].append(a)

  visited = set([node_A])
  q = collections.deque([node_A])

  while q:
    e = q.popleft()
    visited.add(e)
    if e == node_B: return True
    for neighbor in adj[e]:
      if neighbor not in visited:
        q.append(neighbor)

  return False


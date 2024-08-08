# O(E) / O(V)

def connected_components_count(graph):
  
  if not graph: return 0
  visited = set()
  tot = 0
  
  def dfs(k):
    
    if k in visited: return
    visited.add(k)
    for n in graph[k]:
      if n not in visited:
        dfs(n)

  for k in graph:

    if k not in visited:
      tot += 1
      dfs(k)

  return tot
    
# O(e + v) / O(n)

def has_path(graph, src, dst):

  stack = [src]
  visited = set([src])
  
  while stack:

    curr = stack.pop()
    if curr == dst:
       return True
    visited.add(curr)
    for neighbor in graph[curr]:
      if neighbor not in visited:
        stack.append(neighbor)

  return False
    
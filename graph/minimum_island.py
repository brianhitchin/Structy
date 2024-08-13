# O(r * c), O(r * c)

def minimum_island(grid):

  visited = set()
  ROWS, COLS = len(grid), len(grid[0])
  
  def dfs(r, c):
    
    if (r, c) in visited: return 
    area = 1
    visited.add((r, c))
    
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in delta:
      nr, nc = r + dr, c + dc
      if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 'L':
        area += dfs(nr, nc)

    return area

  area = float('inf')
  for r in range(ROWS):
    for c in range(COLS):
      if (r, c) not in visited and grid[r][c] == 'L':
        area = min(area, dfs(r, c))

  return area

    

    
    
# O(r * c), O(r * c)

def island_count(grid):

  visited = set()
  ROWS, COLS = len(grid), len(grid[0])
  
  def dfs(r, c):
    
    if (r, c) in visited: return
    visited.add((r, c))
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dr, dc in delta:
      nr = r + dr
      nc = c + dc
      if (nr, nc) not in visited and 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 'L':
        dfs(nr, nc)

  total = 0
  for r in range(ROWS):
    for c in range(COLS):
      if (r, c) not in visited and grid[r][c] == 'L':
        dfs(r, c)
        total += 1

  return total

    
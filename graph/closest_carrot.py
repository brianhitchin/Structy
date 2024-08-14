# O(r * c), O(r * c)

import collections

def closest_carrot(grid, starting_row, starting_col):

  q = collections.deque([(starting_row, starting_col, 0)])
  visited = set()
  ROWS, COLS = len(grid), len(grid[0])

  while q:

    r, c, d = q.popleft()
    if grid[r][c] == 'C':
      return d
    visited.add((r, c))
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dr, dc in delta:
      nr, nc = r + dr, c + dc
      if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and (grid[nr][nc] == 'O' or grid[nr][nc] == 'C'):
        q.append((nr, nc, d + 1))

  return -1
# O(n) / O(n)

def depth_first_values(root):

  res = []

  def dfs(root):

    if not root: return
    res.append(root.val)
    dfs(root.left)
    dfs(root.right)

  dfs(root)
  return res
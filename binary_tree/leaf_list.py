# O(n) / O(n)

def leaf_list(root):

  res = []

  def recurse(root):

    if not root: return

    if not root.left and not root.right: res.append(root.val)

    recurse(root.left)
    recurse(root.right)

  recurse(root)
  return res
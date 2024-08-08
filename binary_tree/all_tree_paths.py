def all_tree_paths(root):

  res = []
  chkr = set()
  
  def backtrack(root, arr = []):

    if not root: return

    arr.append(root.val)
    
    if not root.left and not root.right:
      
      newArr = arr.copy()
      tnewArr = tuple(newArr)
      
      if tnewArr not in chkr:
        chkr.add(tnewArr)
        res.append(newArr)

      arr.pop()
      return  

    backtrack(root.left, arr)
    backtrack(root.right, arr)
    
    arr.pop()

  backtrack(root)
  return res
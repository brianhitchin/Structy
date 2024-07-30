# O(n) / O(1)

def compress(s):

  cur, val = '', 0
  res = ""
    
  for char in s:
    
    if char != cur:
      
      if val:

        res += str(val) + cur if val > 1 else cur
          
      cur = char
      val = 1

    else:
      val += 1

  if val:

    res += str(val) + cur if val > 1 else cur
  
  return res
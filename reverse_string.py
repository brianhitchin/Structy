# O(n^2) / O(n^2)
# Slicing is O(n)

def reverse_string(s):
  
  if not s: return ""

  return s[-1] + reverse_string(s[:len(s) - 1])

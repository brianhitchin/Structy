# O(n + m) / O(n) where n = len(a)

def intersection(a, b):

  sa = set(a)
  return [i for i in b if i in sa]
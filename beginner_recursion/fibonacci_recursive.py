# O(2^n) / O(n) - call of the height stack will be the height of the "tree"

def fibonacci(n):

  if n < 2:
    return n

  return fibonacci(n - 1) + fibonacci(n - 2)

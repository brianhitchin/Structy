# O(n) / O(n)

def fib(n):

  def subFib(n):

    if n in d:
      return d[n]

    d[n] = subFib(n-1) + subFib(n-2)
    return d[n]
  
  d = {0: 0, 1: 1, 2: 1}
  return subFib(n)

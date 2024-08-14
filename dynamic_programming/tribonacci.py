# O(n) / O(n)

def tribonacci(n):

  memo = {0: 0, 1: 0, 2: 1}

  def helper(n):

    if n in memo:
      return memo[n]

    memo[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
    return memo[n]

  return helper(n)
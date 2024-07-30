def is_prime(n):

  # To save on time, we can check up to the square root of the n,
  # as sqrt(n) * sqrt(n) == n. No need to check further.
  # O(sqrt(n)) / O(1)

  # base case
  if n == 1: return False
  
  for num in range(2, int(n ** 1/2) + 1):
    if not n % num: return False
  return True
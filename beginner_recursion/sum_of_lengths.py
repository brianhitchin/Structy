# O(n) / O(n) - call stack

def sum_of_lengths(strings):

  if not strings: return 0

  poppedString = strings.pop()
  return len(poppedString) + sum_of_lengths(strings)

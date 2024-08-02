# O(n^2) / O(n^2)

def palindrome(s):

  if len(s) == 0 or len(s) == 1:
    return True

  return s[0] == s[-1] and palindrome(s[1:len(s)-1])
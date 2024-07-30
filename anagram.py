# 1 - Counter
# O(n) where n is the longer len between s1 and s2.

import collections

def anagrams(s1, s2):

  return collections.Counter(s1) == collections.Counter(s2)
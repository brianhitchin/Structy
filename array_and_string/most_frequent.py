# By iterating "char in s", we can ensure that whatever comes first stays if equal.
# O(2N) / O(n) where n = unique char in s.

import collections

def most_frequent_char(s):

  c = collections.Counter(s)
  mostFreq = None

  for char in s:
    if mostFreq is None or c[char] > c[mostFreq]:
      mostFreq = char

  return mostFreq
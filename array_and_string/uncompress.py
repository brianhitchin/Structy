# O(n) / O(m)
# m = biggest number

def uncompress(s):

  # set to optimize look up
  nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
  # two pointer, j moves forward when number is encountered
  i, j = 0, 0
  res = ""

  while j < len(s):

    if s[j] in nums:
      j += 1
      
    else:
      mult = int(s[i:j])
      res += s[j] * mult
      j += 1
      i = j

  return res
      
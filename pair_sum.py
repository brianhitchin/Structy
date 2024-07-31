# O(n) / O(n)

def pair_sum(numbers, target_sum):

  d = {}

  for i in range(len(numbers)):
    target = target_sum - numbers[i]
    if target in d:
      return (d[target], i)
    d[numbers[i]] = i
def pair_product(numbers, target_product):

  d = {}

  for i in range(len(numbers)):

    target = target_product / numbers[i]
    if target in d:
      return (d[target], i)

    d[numbers[i]] = i
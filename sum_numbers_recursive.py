# O(n) / O(n) - call stack

def sum_numbers_recursive(numbers):

  def recurse(arr, sum):
    
    if not arr: return sum
    val = arr.pop()
    return recurse(arr, sum + val)

  totalSum = recurse(numbers, 0)
  return totalSum

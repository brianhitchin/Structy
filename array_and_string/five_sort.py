# O(n) / O(1)
# keep going left until right is no longer 5
# then check for possibility of swap

def five_sort(nums):

  i, j = 0, len(nums) - 1

  while i < j:

    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1
    else:
      i += 1

  return nums
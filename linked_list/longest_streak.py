# O(n) / O(1)

def longest_streak(head):

  prev, longest, inter = None, 0, 0

  while head:
    if not prev:
      prev = head.val
      inter = 1
    elif head.val == prev:
      inter += 1
    else:
      longest = max(longest, inter)
      inter = 1
      prev = head.val

    head = head.next

  longest = max(longest, inter)
  return longest
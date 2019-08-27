# Definition for singly-linked list.
class ListNode(object):

  def __init__(self, x):
    self.val = x
    self.next = None

############### my code START ###################

  # helper function to calculate length of the entire list starting from "self"
  def getLength(self):
    length = 1
    pointer = self
    while (pointer.next is not None):
      pointer = pointer.next
      length = length + 1
    return length


class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    l1_length = l1.getLength()
    l2_length = l2.getLength()
    max_length = l1_length if (l1_length > l2_length) else l2_length
 
    l1_pointer = l1
    l2_pointer = l2

    result = ListNode(0)
    pointer = result
    sum = l1_pointer.val + l2_pointer.val
    pointer.val = sum % 10
    carry = sum / 10

    # todo edge case what if two lists have different lengths
    for digit_pow in range(2,max_length+1):
      l1_pointer = l1_pointer.next #points to the next digits to be added
      l2_pointer = l2_pointer.next
      sum = l1_pointer.val + l2_pointer.val
      pointer.next = ListNode((sum + carry) % (10))
      pointer = pointer.next
      carry = (sum + carry) / (10)

    return result
      

################## my code END ###################


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8

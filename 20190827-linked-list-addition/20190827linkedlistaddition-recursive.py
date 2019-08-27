# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
############################# my solution START ############################
    solution = ListNode(0)

    sum = l1.val + l2.val + c
    digit = sum % 10
    c = sum / 10
    solution.val = digit

    if l1.next is not None:
      solution.next = Solution.addTwoNumbers(self, l1.next, l2.next, c)
    return solution
############################### my solution END ##########################


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

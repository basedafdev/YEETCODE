class ListNode:
  def __init__(self, x):         
    self.val = x
    self.next = None
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
    carry = 0
    sumNode = ListNode(0)
    head = sumNode
    while (l1 is not None or l2 is not None):
      if (l1 is not None and l2 is None):
        value = l1.val + carry
        newNode = ListNode(value % 10)
        sumNode.next = newNode
        sumNode = newNode
        carry = value // 10
        l1 = l1.next
      elif (l1 is None and l2 is not None):
        value = l2.val + carry
        newNode = ListNode(value % 10)
        sumNode.next = newNode
        sumNode = newNode
        carry = value // 10
        l2 = l2.next
      else:
        value = l1.val + l2.val + carry
        newNode = ListNode(value % 10)
        sumNode.next = newNode
        sumNode = newNode
        carry = value // 10
        l1 = l1.next
        l2 = l2.next
    if (carry > 0):
      sumNode.next = ListNode(carry)
    return head.next
if __name__ == "__main__":
  head1 = ListNode(1)
  head1.next = ListNode(8)
  head2 = ListNode(0)
  x = Solution()
  x.addTwoNumbers(head1,head2)
  

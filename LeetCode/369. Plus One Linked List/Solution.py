# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry = self.plus(head)

        if carry:
            return ListNode(carry, head)

        return head


    def plus(self, node: ListNode) -> int:
        if node.next:
            carry = self.plus(node.next)
            sum = node.val + carry
        else:
            sum = node.val + 1


        if sum >= 10:
            node.val = sum % 10
            return 1
        else:
            node.val = sum
            return 0

        

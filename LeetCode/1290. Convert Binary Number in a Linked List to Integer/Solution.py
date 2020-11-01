# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        it = head
        ret = 0

        while it:
            ret = ret * 2 + it.val
            it = it.next

        return ret

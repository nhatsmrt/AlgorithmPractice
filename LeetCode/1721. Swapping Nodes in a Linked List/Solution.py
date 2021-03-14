# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Time and Space Complexity: O(N)

        data = []

        while head:
            data.append(head.val)
            head = head.next

        tmp = data[k - 1]
        data[k - 1] = data[-k]
        data[-k] = tmp

        ret = ListNode(data[0])
        it = ret

        for datum in data[1:]:
            it.next = ListNode(datum)
            it = it.next

        return ret

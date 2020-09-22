"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node
        else:
            it = head

            while it.next != head and it.val <= it.next.val:
                it = it.next

            it = it.next

            low = it
            high = it.next

            while high != it and (low.val > insertVal or high.val < insertVal):
                low = high
                high = high.next

            new_node.next = high
            low.next = new_node

        return head

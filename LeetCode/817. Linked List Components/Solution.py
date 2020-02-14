# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Set

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        return self.recursion(head, False, set(G))

    def recursion(self, node: ListNode, in_comp: bool, Gset: Set[int]) -> int:
        if node is None:
            return 1 if in_comp else 0

        if node.val not in Gset and in_comp:
            return 1 + self.recursion(node.next, False, Gset)

        return self.recursion(node.next, node.val in Gset, Gset)
        

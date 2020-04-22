# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Tuple

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # KMP on Tree
        # Time and Space Complexity: O(M + N)

        arr, lps = self.process(head)
        return self.match(root, arr, lps, 0)

    def match(self, node: TreeNode, arr: List[int], lps: List[int], list_ind: int) -> bool:
        if node.val == arr[list_ind]:
            list_ind += 1

            if list_ind == len(arr):
                return True

        else:
            if list_ind > 0:
                list_ind = lps[list_ind - 1]
                return self.match(node, arr, lps, list_ind)

        return (node.left is not None and self.match(node.left, arr, lps, list_ind)) or (node.right is not None and self.match(node.right, arr, lps, list_ind))


    def process(self, node: ListNode) -> Tuple[List[int], List[int]]:
        arr = self.array(node)

        max_len = 0
        lps = [0] * len(arr)
        i = 1

        while i < len(arr):
            if arr[i] == arr[max_len]:
                # match:
                max_len += 1
                lps[i] = max_len
                i += 1
            elif max_len > 0:
                max_len = lps[max_len - 1]
            else:
                lps[i] = 0
                i += 1

        return arr, lps

    def array(self, node: ListNode) -> int:
        ret = []
        while node is not None:
            ret.append(node.val)
            node = node.next

        return ret

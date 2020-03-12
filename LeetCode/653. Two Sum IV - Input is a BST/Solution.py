# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False

        data = []
        self.in_order(root, data)

        start = 0
        end = len(data) - 1

        while start < end:
            cand = data[start] + data[end]
            if cand == k:
                return True
            elif cand < k:
                start += 1
            else:
                end -= 1

        return False

    def in_order(self, node: TreeNode, data: List[int]):
        if node is not None:
            self.in_order(node.left, data)
            data.append(node.val)
            self.in_order(node.right, data)
        

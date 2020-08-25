# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        level = [root]
        missing = False

        while level:
            next_level = []

            for node in level:
                if missing and any((node.left, node.right)):
                    return False
                elif node.right and not node.left:
                    return False

                if node.left:
                    next_level.append(node.left)
                else:
                    missing = True

                if node.right:
                    next_level.append(node.right)
                else:
                    missing = True
            level = next_level

        return True

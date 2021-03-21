# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # Time and Space Complexity: O(N)

        level = [root]
        leftmost = None

        while level:
            leftmost = level[0].val

            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)

                if node.right:
                    new_level.append(node.right)

            level = new_level

        return leftmost

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # Time Complexity: O(H 2^H)
        # Space Complexity: O(H) extra space

        return self.backtrack(root, [str(root.val)], [])

    def backtrack(self, node, partial, ret):
        if not (node.left or node.right): # leaf
            ret.append("->".join(partial))
        else:
            if node.left:
                partial.append(str(node.left.val))
                self.backtrack(node.left, partial, ret)
                partial.pop()

            if node.right:
                partial.append(str(node.right.val))
                self.backtrack(node.right, partial, ret)
                partial.pop()

        return ret

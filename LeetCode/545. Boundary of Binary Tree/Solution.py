# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_leaf(node: TreeNode) -> bool:
    return not (node.left or node.right)

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # Time and Space Complexity: O(N)

        if not root:
            return []

        ret = [root.val]
        self.get_boundary(root.left, True, False, ret)
        self.get_boundary(root.right, False, True, ret)

        return ret

    def get_boundary(
        self, node: TreeNode, is_leftmost: bool, is_rightmost: bool, ret: List[int]
    ):
        if node:
            if is_leftmost:
                ret.append(node.val)

            self.get_boundary(node.left, is_leftmost, is_rightmost and not node.right, ret)
            self.get_boundary(node.right, is_leftmost and not node.left, is_rightmost, ret)

            if not is_leftmost and (is_rightmost or is_leaf(node)):
                ret.append(node.val)

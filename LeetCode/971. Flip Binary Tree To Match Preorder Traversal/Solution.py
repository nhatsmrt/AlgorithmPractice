# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)

        ret = []
        check, boundary = self.check(root, voyage, 0, ret)

        if check and boundary == len(voyage):
            return ret

        return [-1]

    def check(self, node: TreeNode, voyage: List[int], i: int, ret: List[int]):
        if node.val != voyage[i]:
            return (False, -1)

        if not (node.left or node.right):  # if a leaf
            return (True, i + 1)

        if i + 1 == len(voyage):
            return (False, -1)

        if not (node.left and node.right): # only one child
            child = node.left if node.left else node.right
            return self.check(child, voyage, i + 1, ret)

        if node.left.val == voyage[i + 1]:  # no flip needed
            left_check, left_boundary = self.check(node.left, voyage, i + 1, ret)

            if left_check and left_boundary < len(voyage):
                return self.check(node.right, voyage, left_boundary, ret)
            else:
                return (False, -1)

        elif node.right.val == voyage[i + 1]:
            ret.append(node.val)

            right_check, right_boundary = self.check(node.right, voyage, i + 1, ret)

            if right_check and right_boundary < len(voyage):
                return self.check(node.left, voyage, right_boundary, ret)
            else:
                return (False, -1)

        else:
            return (False, -1)

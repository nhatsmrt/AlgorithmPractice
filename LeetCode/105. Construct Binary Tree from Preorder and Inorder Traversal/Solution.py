# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time and Space Complexity: O(N)

        inorder_index = {value: i for i, value in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            root_val = preorder[pre_start]

            in_root_ind = inorder_index[root_val]
            left_size = in_root_ind - in_start
            right_size = in_end - in_root_ind

            left = None if left_size == 0 else build(pre_start + 1, pre_start + left_size, in_start, in_root_ind - 1)
            right = None if right_size == 0 else build(pre_start + left_size + 1, pre_end, in_root_ind + 1, in_end)

            return TreeNode(root_val, left, right)

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

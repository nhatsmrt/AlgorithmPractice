# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # Time and Space Complexity: O(N)

        cur_level = [root]
        ret = []

        while cur_level:
            ret.append(sum(map(lambda node: node.val, cur_level)) / len(cur_level))
            next_level = []

            for node in cur_level:
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            cur_level = next_level

        return ret

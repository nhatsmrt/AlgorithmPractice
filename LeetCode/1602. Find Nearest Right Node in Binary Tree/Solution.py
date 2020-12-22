# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        # Time and Space Complexity: O(N)

        cur_level, cur_index = [root], {root: 0}

        while True:
            if u in cur_index:
                if cur_index[u] == len(cur_level) - 1:
                    return None

                return cur_level[cur_index[u] + 1]

            else:
                next_level, next_index = [], {}

                for node in cur_level:
                    if node.left is not None:
                        next_index[node.left] = len(next_level)
                        next_level.append(node.left)

                    if node.right is not None:
                        next_index[node.right] = len(next_level)
                        next_level.append(node.right)


                cur_level, cur_index = next_level, next_index

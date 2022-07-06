# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(H)

        p_path = self.find_path_to_node(root, p, [])
        q_path = self.find_path_to_node(root, q, [])

        i = 0
        while i + 1 < min(len(p_path), len(q_path)) and p_path[i + 1] == q_path[i + 1]:
            i += 1

        return len(p_path) + len(q_path) - i * 2 - 2

    def find_path_to_node(self, node: TreeNode, targ: List[int], ret: List[TreeNode]) -> List[TreeNode]:
        if not node:
            return ret

        ret.append(node.val)
        if node.val == targ:
            return ret


        for child in [node.left, node.right]:
            self.find_path_to_node(child, targ, ret)

            if ret[-1] == targ:
                break
        else:
            ret.pop() # targ not in subtree

        return ret

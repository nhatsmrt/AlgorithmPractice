# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0

        euler = []
        begin = {}
        end = {}
        self.flatten(root, euler, begin, end, 0)

        diff_sq = []
        for i in range(1, len(euler)):
            diff_sq.append((euler[i] - euler[i - 1]) ** 2)


        prefixes = [0]
        for val in diff_sq:
            prefixes.append(prefixes[-1] + val)

        ret = 0
        for node in begin:
            node_val = euler[begin[node]]

            if prefixes[end[node]] - prefixes[begin[node]] == 0:
                ret += 1

        return ret

    def flatten(
        self, node: TreeNode, euler: List[int],
        begin: dict, end: dict, time: int
    ) -> int:
        euler.append(node.val)
        begin[node] = time
        time += 1

        if node.left is not None:
            time = self.flatten(node.left, euler, begin, end, time)

        if node.right is not None:
            time = self.flatten(node.right, euler, begin, end, time)

        euler.append(node.val)
        end[node] = time
        return time + 1
        

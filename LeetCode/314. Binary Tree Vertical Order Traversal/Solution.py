# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        nodes = {}
        queue = deque()
        queue.append((root, 0))
        min_x = 0
        max_x = 0

        while len(queue) > 0:
            node, x = queue.popleft()
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            if x not in nodes:
                nodes[x] = []
            nodes[x].append(node.val)
            if node.left is not None:
                queue.append((node.left, x - 1))

            if node.right is not None:
                queue.append((node.right, x + 1))

        ret = []
        for i in range(min_x, max_x + 1):
            ret.append(nodes[i])

        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ret = []
        queue = collections.deque()
        queue.append((root, 0))

        while len(queue) > 0:
            node, level = queue.popleft()
            if len(ret) == level:
                ret.append([])
            ret[level].append(node.val)

            if node.left != None:
                queue.append((node.left, level + 1))

            if node.right != None:
                queue.append((node.right, level + 1))

        return reversed(ret)

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Time Complexity: O(|V|), Space Complexity: O(|V|)
        if K == 0:
            return [target.val]

        ret = []
        self.traverse(target.left, K - 1, ret, 'n')
        self.traverse(target.right, K - 1, ret, 'n')

        ancestry, direction = self.find_parent(root, target)
        bound = min(K, len(ancestry))
        for i in range(bound):
            self.traverse(ancestry[i], K - i - 1, ret, direction[i])

        return ret

    def find_parent(self, node: TreeNode, target: TreeNode):
        if node is None or node == target:
            return [], []

        if node.left == target:
            return [node], ['l']

        if node.right == target:
            return [node], ['r']

        paths, directions = self.find_parent(node.left, target)
        if len(paths) > 0:
            paths.append(node)
            directions.append('l')
            return paths, directions

        paths, directions = self.find_parent(node.right, target)
        if len(paths) > 0:
            paths.append(node)
            directions.append('r')
            return paths, directions

        return [], []

    def traverse(self, node: TreeNode, dist: int, ret: List[TreeNode], ban_dir: str):
        if node is not None:
            if dist == 0:
                ret.append(node.val)
            else:
                if ban_dir != 'l':
                    self.traverse(node.left, dist - 1, ret, 'n')
                if ban_dir != 'r':
                    self.traverse(node.right, dist - 1, ret, 'n')

        

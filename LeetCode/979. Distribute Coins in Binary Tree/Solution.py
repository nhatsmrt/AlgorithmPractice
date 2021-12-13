# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Time and Space Complexity: O(N)

        self.sizes = {}
        self.coins = {}

        self.compute(root)

        return self.distribute(root)

    def distribute(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        num_moves = self.distribute(node.left) + self.distribute(node.right)

        excess = max(0, self.coins[node] - self.sizes[node])
        transfer_left = max(0, self.sizes.get(node.left, 0) - self.coins.get(node.left, 0))
        transfer_right = max(0, self.sizes.get(node.right, 0) - self.coins.get(node.right, 0))

        num_moves += transfer_left + transfer_right + excess
        return num_moves

    def compute(self, node):
        size, coin = 1, node.val

        if node.left:
            size_left, coin_left = self.compute(node.left)
            size += size_left
            coin += coin_left

        if node.right:
            size_right, coin_right = self.compute(node.right)
            size += size_right
            coin += coin_right

        self.sizes[node] = size
        self.coins[node] = coin

        return size, coin

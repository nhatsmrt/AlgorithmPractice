# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_leaf(node: TreeNode):
    return node and not (node.left or node.right)

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # Time and Space Complexity: O(N)

        adj_lists = {}
        leaves = set()

        self.dfs(root, None, adj_lists, leaves)

        in_deque = set([k])
        to_check = deque()
        to_check.append((k, 0))

        while len(to_check) > 0:
            node, dist = to_check.popleft()

            if node in leaves:
                return node

            for neighbor in adj_lists[node]:
                if neighbor not in in_deque:
                    in_deque.add(neighbor)
                    to_check.append((neighbor, dist + 1))


    def dfs(self, node: TreeNode, par: TreeNode, adj_lists: dict, leaves: dict):
        if is_leaf(node):
            leaves.add(node.val)

        adj_lists[node.val] = []

        if par:
            adj_lists[node.val].append(par.val)

        if node.left:
            adj_lists[node.val].append(node.left.val)
            self.dfs(node.left, node, adj_lists, leaves)

        if node.right:
            adj_lists[node.val].append(node.right.val)
            self.dfs(node.right, node, adj_lists, leaves)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import reduce

def special_min(val1: int, val2: int) -> int:
        if val1 == -1:
            return val2
        if val2 == -1:
            return val1

        return min(val1, val2)

def add(val1: int, val2: int) -> int:
    if val1 == -1 or val2 == -1:
            return -1

    return val1 + val2


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # dp[node][0] = number of camera needed to monitor subtree rooted at node,
        # if a cameria is installed at node
        # dp[node][1] = number of camera needed to monitor subtree rooted at node,
        # if a camera is not installed at node but at node's parent
        # dp[node][2] = number of camera needed to monitor subtree rooted at node,
        # if a cameria is not installed at node or node's parent (but at one of node's children)

        # Time and space complexity: O(n)

        self.dp = {}

        self.dfs(root)
        self.dp[root][1] = -1

        return min([val for val in self.dp[root] if val != -1])


    def dfs(self, node: TreeNode):
        self.dp[node]= [1, 0, -1]

        children = []
        if node.left is not None:
            children.append(node.left)
            self.dfs(node.left)

        if node.right is not None:
            children.append(node.right)
            self.dfs(node.right)

        if len(children) == 0:
            # Leaf:
            self.dp[node] = [1, 0, -1]
        elif len(children) == 1:
            child = children[0]
            self.dp[node][0] = add(1, special_min(self.dp[child][0], self.dp[child][1]))
            self.dp[node][1] = special_min(self.dp[child][0], self.dp[child][2])
            self.dp[node][2] = self.dp[child][0]
        else:
            left, right = children[0], children[1]

            # If a camera is placed at node:
            left_best = special_min(self.dp[left][0], self.dp[left][1])
            right_best = special_min(self.dp[right][0], self.dp[right][1])
            self.dp[node][0] = add(add(1, left_best), right_best)

            # If no camera is placed at node, but one is placed at its parent
            left_best = special_min(self.dp[left][0], self.dp[left][2])
            right_best = special_min(self.dp[right][0], self.dp[right][2])
            self.dp[node][1] = add(left_best, right_best)

            # If no camera is placed at node or its parent:
            first_candidate = add(
                self.dp[left][0],
                special_min(self.dp[right][0], self.dp[right][2])
            )
            second_candidate = add(
                self.dp[right][0],
                special_min(self.dp[left][0], self.dp[left][2])
            )
            self.dp[node][2] = special_min(first_candidate, second_candidate)

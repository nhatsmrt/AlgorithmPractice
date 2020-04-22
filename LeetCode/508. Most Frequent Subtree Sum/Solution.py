# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        euler = []
        begin = {}
        end = {}

        self.flatten(root, euler, begin, end, 0)

        prefixes = [0]
        for num in euler:
            prefixes.append(prefixes[-1] + num)

        counter = Counter()
        for node in begin:
            counter[(prefixes[end[node] + 1] - prefixes[begin[node]]) // 2] += 1

        most_freq = 0
        ret = []

        for subtree_sum in counter:
            if counter[subtree_sum] == most_freq:
                ret.append(subtree_sum)
            elif counter[subtree_sum] > most_freq:
                most_freq = counter[subtree_sum]
                ret = [subtree_sum]

        return ret

    def flatten(self, node: TreeNode, euler: List[int], begin: dict, end: dict, time: int) -> time:
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

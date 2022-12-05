# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def merge(ret, small_level, small_cnter, big_level, big_cnter, distance):
    ret_level = big_level + 1
    ret_cnter = big_cnter

    for fake_dist in small_cnter:
        real_dist = fake_dist + small_level

        target = distance - 2 - real_dist - big_level

        for fake_dist_big in big_cnter:
            if fake_dist_big <= target:
                ret += big_cnter[fake_dist_big] * small_cnter[fake_dist]

    for fake_dist in small_cnter:
        real_dist = fake_dist + small_level
        big_cnter[real_dist - big_level] += small_cnter[fake_dist]

    return ret, (ret_level, ret_cnter)

def count(node: TreeNode, distance: int):
    if not node:
        return 0, (0, Counter())

    if not (node.left or node.right):
        cnter = Counter()
        cnter[0] = 1
        return (0, (0, cnter))

    left_ret, (left_level, left_cnter) = count(node.left, distance)
    right_ret, (right_level, right_cnter) = count(node.right, distance)

    ret = left_ret + right_ret

    if len(left_cnter) < len(right_cnter):
        ret = merge(ret, left_level, left_cnter, right_level, right_cnter, distance)
    else:
        ret = merge(ret, right_level, right_cnter, left_level, left_cnter, distance)

    return ret

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N log N)
        return count(root, distance)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Time and Space Complexity: O(n)

        return self.bstify(nums, 0, len(nums) - 1)

    def bstify(self, nums: List[int], low: int, high: int) -> TreeNode:
        if low > high:
            return None

        if low == high:
            return TreeNode(nums[low])

        mid = (high + low) // 2
        ret = TreeNode(nums[mid])
        ret.left = self.bstify(nums, low, mid - 1)
        ret.right = self.bstify(nums, mid + 1, high)

        return ret

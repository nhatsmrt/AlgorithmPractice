# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Time Complexity: O(log(N)^2)
        # Space Complexity: O(log(N))

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        height = 0
        it = root

        while it is not None:
            height += 1
            it = it.left

        low = 2 ** (height - 1) - 1
        high = 2 ** height - 2

        while low < high:
            # print(low, high)
            mid = high - (high - low) // 2
            # print(mid)

            if self.is_valid(root, mid):
                low = mid
            else:
                high = mid - 1

        return low + 1

    def is_valid(self, root: TreeNode, ind: int) -> bool:
        path = self.get_path(ind)
        it = root

        for step in path:
            if step == 0:
                if it.left is None:
                    return False
                it = it.left

            elif step == 1:
                if it.right is None:
                    return False
                it = it.right

        return True

    def get_path(self, ind: int) -> List[int]:
        ret = []
        while ind > 0:
            ret.append(1 - ind % 2)
            ind = (ind - 1) // 2

        return ret[::-1]

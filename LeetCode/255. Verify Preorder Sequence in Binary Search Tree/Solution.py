INF = 1000000


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(H)

        return self.verify(preorder, 0, -INF, INF) == len(preorder)

    def verify(self, preorder: List[int], i: int, lower: int, upper: int):
        if i >= len(preorder):
            return i

        if preorder[i] <= lower or preorder[i] >= upper:
            return i

        left_end = self.verify(preorder, i + 1, lower, preorder[i])
        right_end = self.verify(preorder, left_end, preorder[i], upper)

        return right_end

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Time and Space Complexity: O(MN)

        self.dp = [[-1 for _ in range(len(nums2))] for _ in range(len(nums1))]
        candidate = self.build(nums1, nums2, 0, 0)

        if candidate == 0:
            return max(min(nums1) * max(nums2), min(nums2) * max(nums1))

        return candidate

    def build(self, nums1: int, nums2: int, i: int, j: int) -> int:
        if i == len(nums1) or j == len(nums2):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        ret = max(
            self.build(nums1, nums2, i + 1, j),
            self.build(nums1, nums2, i, j + 1),
            nums1[i] * nums2[j] + self.build(nums1, nums2, i + 1, j + 1)
        )

        self.dp[i][j] = ret
        return ret
        

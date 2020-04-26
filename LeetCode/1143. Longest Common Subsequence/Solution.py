class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time and Space Complexity: O(MN)

        self.dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        return self.lcsFrom(text1, text2, 0, 0)

    def lcsFrom(self, text1: str, text2: str, i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        ret = max(self.lcsFrom(text1, text2, i, j + 1), self.lcsFrom(text1, text2, i + 1, j))
        if text1[i] == text2[j]:
            ret = max(ret, 1 + self.lcsFrom(text1, text2, i + 1, j + 1))

        self.dp[i][j] = ret
        return ret

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.dp = [[-1 for j in range(len(B))] for i in range(len(A))]
        return self.match(A, B, 0, 0)

    def match(self, A: List[int], B: List[int], i: int, j: int) -> int:
        if i == len(A) or j == len(B):
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        ret = max(self.match(A, B, i + 1, j), self.match(A, B, i, j + 1))

        if A[i] == B[j]:
            ret = max(ret, 1 + self.match(A, B, i + 1, j + 1))

        self.dp[i][j] = ret
        return ret

class Solution:
    _dp = {}

    def integerReplacement(self, n: int) -> int:
        # Time and Space Complexity: O(N)

        if n in self._dp:
            return self._dp[n]

        if n == 1:
            ret = 0
        elif n % 2 == 0:
            ret = 1 + self.integerReplacement(n // 2)
        else:
            ret = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

        self._dp[n] = ret
        return ret

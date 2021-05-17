class Solution:
    _MOD = 1000000007

    def rearrangeSticks(self, n: int, k: int) -> int:
        # Time and Space Complexity: O(NK)

        # dp[n, k] = sum_{i = k - 1}^{n - 1} (n - 1 choose i) dp[i, k - 1] (n - i - 1)!
        # = sum_{i = k - 1}^{n - 1} (n - 1)! / i! * dp[i, k - 1]
        # = sum_{i = k - 1}^{n - 1} range_prod(i + 1, n - 1) * dp[i, k - 1]
        # = dp[n - 1, k - 1] + (n - 1) * dp[n - 1, k]

        self.dp = {}
        self.factorials = [1]

        for i in range(1, n + 1):
            self.factorials.append((self.factorials[-1] * i) % self._MOD)

        return self.num_sols(n, k)

    def num_sols(self, n: int, k: int) :
        key = (n, k)
        if key in self.dp:
            return self.dp[key]

        if n == k:
            ret = 1
        elif k == 1:
            ret = self.factorials[n - 1]
        else:
            ret = (n - 1) * self.num_sols(n - 1, k)
            ret %= self._MOD

            ret += self.num_sols(n - 1, k - 1)
            ret %= self._MOD

        self.dp[key] = ret
        return ret

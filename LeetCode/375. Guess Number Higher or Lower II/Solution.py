class Solution:
    def getMoneyAmount(self, n: int) -> int:
        self.dp = [[-1] * n for i in range(n)]
        return self.minMoney(1, n)

    def minMoney(self, low: int, high: int):
        if low >= high:
            return 0

        if self.dp[low - 1][high - 1] != -1:
            return self.dp[low - 1][high - 1]

        ret = 1000000
        for k in range(low, high + 1):
            candidate = k + max(self.minMoney(k + 1, high), self.minMoney(low, k - 1))
            ret = min(candidate, ret)

        self.dp[low - 1][high - 1] = ret
        return ret

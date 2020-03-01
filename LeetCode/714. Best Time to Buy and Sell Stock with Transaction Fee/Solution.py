class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Time and Space Complexity: O(N)
        self.dp = [[None] * len(prices), [None] * len(prices)]
        return self.maxProfitDP(prices, fee, 0, 0)

    def maxProfitDP(self, prices: List[int], fee: int, i: int, status: int) -> int:
        if i == len(prices):
            return 0

        if self.dp[status][i] is not None:
            return self.dp[status][i]

        if status == 0:
            # currently not holding stock
            candidate1 = self.maxProfitDP(prices, fee, i + 1, 0)
            candidate2 = -prices[i] + self.maxProfitDP(prices, fee, i + 1, 1)
            ret = max(candidate1, candidate2)
        else:
            candidate1 = self.maxProfitDP(prices, fee, i + 1, 1)
            candidate2 = prices[i] - fee + self.maxProfitDP(prices, fee, i + 1, 0)
            ret = max(candidate1, candidate2)

        self.dp[status][i] = ret
        return ret

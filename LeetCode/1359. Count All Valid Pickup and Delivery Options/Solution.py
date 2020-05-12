class Solution:
    def countOrders(self, n: int) -> int:
        # f(n) = n * f(n - 1) * [2(n - 1) + 1]
        # Time and Space Complexity: O(N)

        MOD = 1000000007

        ret = 1
        for i in range(2, n + 1):
            ret *= i
            ret %= MOD

            ret *= (2 * (i - 1) + 1)
            ret %= MOD

        return ret

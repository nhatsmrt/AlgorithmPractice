class Solution:
    _MOD = 1000000007

    def numWays(self, steps: int, arrLen: int) -> int:
        # Time Complexity: O(S min(S, L))
        # Space Complexity: O(min(S, L))

        def get_max_pos(remaining_steps):
            return min(arrLen, steps - remaining_steps)

        dp = [1] + ([0] * (get_max_pos(0)))

        for remaining_steps in range(1, steps + 1):
            next_dp = []

            for pos in range(get_max_pos(remaining_steps) + 1):
                num_ways = dp[pos]
                if pos < arrLen - 1:
                    num_ways += dp[pos + 1]
                    num_ways %= self._MOD


                if pos > 0:
                    num_ways += dp[pos - 1]
                    num_ways %= self._MOD
                next_dp.append(num_ways)

            dp = next_dp

        return dp[0]

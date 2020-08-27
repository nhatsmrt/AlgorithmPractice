class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # Time Complexity: O(N^3 / K)
        # Space Complexity: O(N^2)

        if (len(stones) - 1) % (K - 1) != 0:
            return -1

        dp = [[-1 for j in range(len(stones))] for i in range(len(stones))]

        # DP[i][j] = minimum cost to reduce stones[i] to stones[j] to minimum number of piles

        prefix = [0] + list(itertools.accumulate(stones))

        for l in range(1, K):
            for start in range(0, len(stones) - l + 1):
                dp[start][start + l - 1] = 0

        for i in range(len(stones) - K + 1):
            dp[i][i + K - 1] = prefix[i + K] - prefix[i]

        for l in range(K + 1, len(stones) + 1):
            for start in range(0, len(stones) - l + 1):
                end = start + l - 1

                for mid in range(start, end, K - 1):
                    if dp[start][end] == -1:
                        dp[start][end] = dp[start][mid] + dp[mid + 1][end]
                    else:
                        dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid + 1][end])

                if (l - 1) % (K - 1) == 0:
                    dp[start][end] += prefix[end + 1] - prefix[start]

        return dp[0][len(stones) - 1]

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N^2)

        # Let dp[i][j] = # of moves to remove the subarray from i to j

        # dp[i][i] = 1 for all i
        # dp[i][i + 1] = 1 if arr[i] == arr[i + 1], 2 otherwise.

        # When j >= i + 2, we can reduce arr[i] separately
        # (for 1 + dp[i + 1][j] moves), or "match" arr[i] with an equal value and reduce these two together

        # If we match arr[i] with arr[i + 1], then number of moves is
        # 1 + dp[i + 2][j]

        # If we match arr[i] with some arr[k] (i + 1 < k <= j, arr[i] = arr[k]), it takes
        # dp[i + 1][k - 1] to reduce subarray from i to k
        # (i.e we tag arr[i], arr[k] onto the last step of reducing arr[i + 1: k])
        # and dp[k + 1][j] to reduce the rest of the subarray (if k < j)

        # Taking the minimum of all these posible cases (when they are legal)
        # gives us the final answer.

        self.dp = [[0 for j in range(len(arr))] for i in range(len(arr))]
        return self.reduceCost(arr, 0, len(arr) - 1)

    def reduceCost(self, arr, i: int, j: int) -> int:
        if self.dp[i][j]:
            return self.dp[i][j]

        if i == j:
            ret = 1
        elif i + 1 == j and arr[i] == arr[j]:
            ret = 1
        elif i + 1 == j:
            ret = 2
        else:
            ret = 1 + self.reduceCost(arr, i + 1, j)
            occs = []

            for k in range(i + 1, j + 1):
                if arr[k] == arr[i]:
                    occs.append(k)

            for occ in occs:
                if occ == i + 1:
                    ret = min(ret, 1 + self.reduceCost(arr, i + 2, j))
                else:
                    cand = self.reduceCost(arr, i + 1, occ - 1)
                    if occ != j:
                        cand += self.reduceCost(arr, occ + 1, j)

                    ret = min(ret, cand)

        self.dp[i][j] = ret
        return ret

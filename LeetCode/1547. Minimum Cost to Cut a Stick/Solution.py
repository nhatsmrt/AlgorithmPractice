class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Time and Space Complexity: O(N^2)
        marks = [0] + sorted(cuts) + [n]

        # Let dp[i, j] be the cost of processing the stick from mark[i] to mark[j + 1]
        # dp[i, i] = 0
        # dp[i, j] = C[i, j] + min_{i <= k < j} dp[i, k] + dp[k + 1, j]
        # Answer is dp[0, len(marks) - 2]
        # where C[i, j] = mark[j + 1] - mark[i]

        # Note that the cost matrix satisfy quadrangle and monotone inequality:
        # i <= i' <= j <= j': C[i, j'] + C[i', j] == C[i, j] + C[i', j']
        # i <= i' <= j' <= j: C[i', j'] <= C[i, j]
        # so we can use Knuth-Yao Optimization

        dp = {}
        argmin = {}

        for delta in range(0, len(marks) - 1):
            # compute dp[i, i + delta]
            for i in range(0, len(marks) - 1 - delta):
                j = i + delta

                if not delta:  # base case
                    dp[(i, j)] = 0
                elif delta == 1:
                    best_ind = i
                    dp[(i, j)] = marks[j + 1] - marks[i] + dp[(i, i)] + dp[(j, j)]
                    argmin[(i, j)] = i
                else:
                    best_ind = None
                    best_cost = None

                    for cand_ind in range(argmin[(i, j - 1)], argmin[(i + 1, j)] + 1):
                        if best_ind is None or best_cost > dp[(i, cand_ind)] + dp[(cand_ind + 1, j)]:
                            best_ind = cand_ind
                            best_cost = dp[(i, cand_ind)] + dp[(cand_ind + 1, j)]

                    dp[(i, j)] = best_cost + marks[j + 1] - marks[i]
                    argmin[(i, j)] = best_ind


        return dp[(0, len(marks) - 2)]

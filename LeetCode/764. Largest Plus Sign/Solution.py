class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Time and Space Complexity: O(N^2)

        mine_set = set((mine[0], mine[1]) for mine in mines)

        def build_cum(range_j, reverse):
            ret = [[None for j in range(n)] for i in range(n)]

            for i in range(n):
                cum = 0
                for j in range_j:
                    if reverse:
                        ret[j][i] = cum
                        cum = cum + 1 if (j, i) not in mine_set else 0
                    else:
                        ret[i][j] = cum
                        cum = cum + 1 if (i, j) not in mine_set else 0

            return ret

        left = build_cum(range(n), False)
        right = build_cum(range(n - 1, -1, -1), False)
        up = build_cum(range(n), True)
        down = build_cum(range(n - 1, -1, -1), True)

        ret = 0
        for i in range(n):
            for j in range(n):
                ret = max(ret, int((i, j) not in mine_set) * (1 + min(left[i][j], right[i][j], up[i][j], down[i][j])))

        return ret

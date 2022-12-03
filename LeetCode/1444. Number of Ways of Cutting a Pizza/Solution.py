MOD = 10 ** 9 + 7

class RangeSum2D:
    def __init__(self, arr):
        self.prefixes = [[0 for j in range(len(arr[0]))] for i in range(len(arr))]
        self.prefixes[0][0] = arr[0][0]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                self.prefixes[i][j] = arr[i][j]

                if i:
                    self.prefixes[i][j] += self.prefixes[i - 1][j]

                if j:
                    self.prefixes[i][j] += self.prefixes[i][j - 1]

                if i and j:
                    self.prefixes[i][j] -= self.prefixes[i - 1][j - 1]


    def range_sum(self, row_start, row_end, col_start, col_end):
        ret = self.prefixes[row_end][col_end]

        if row_start:
            ret -= self.prefixes[row_start - 1][col_end]

        if col_start:
            ret -= self.prefixes[row_end][col_start - 1]

        if row_start and col_start:
            ret += self.prefixes[row_start - 1][col_start - 1]

        return ret


def count(summer, row_start, row_end, col_start, col_end, k, solutions):
    key = (row_start, row_end, col_start, col_end, k)

    if key in solutions:
        return solutions[key]

    if k == 1:
        ret = 1 if summer.range_sum(row_start, row_end, col_start, col_end) else 0
    else:
        ret = 0

        # divide horizantally
        for i in range(row_start, row_end):
            if summer.range_sum(row_start, i, col_start, col_end):
                ret += count(summer, i + 1, row_end, col_start, col_end, k - 1, solutions)
                ret %= MOD

        # divide vertically
        for j in range(col_start, col_end):
            if summer.range_sum(row_start, row_end, col_start, j):
                ret += count(summer, row_start, row_end, j + 1, col_end, k - 1, solutions)
                ret %= MOD

    solutions[key] = ret
    return ret

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # Time Complexity: O(M^2 N^2 K (M + N))
        # Space Complexity: O(M^2 N^2 K)

        bin_pizza = list(map(
            lambda row: list(map(lambda entry: 1 if entry == "A" else 0, row)),
            pizza
        ))

        summer = RangeSum2D(bin_pizza)

        return count(summer, 0, len(pizza) - 1, 0, len(pizza[0]) - 1, k, {})

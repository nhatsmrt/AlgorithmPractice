class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time and Space Complexity: O(|strs| m n)
        counts = list(map(Counter, strs))
        self.dp = {}
        return self.solve(counts, 0, n, m)

    def solve(self, counts, i: int, remaining_ones: int, remaining_zeros: int) -> int:
        if i == len(counts):
            return 0

        if (i, remaining_ones, remaining_zeros) in self.dp:
            return self.dp[(i, remaining_ones, remaining_zeros)]

        ret = self.solve(counts, i + 1, remaining_ones, remaining_zeros)

        if remaining_ones >= counts[i]['1'] and remaining_zeros >= counts[i]['0']:
            ret = max(ret, 1 + self.solve(counts, i + 1, remaining_ones - counts[i]['1'], remaining_zeros - counts[i]['0']))

        self.dp[(i, remaining_ones, remaining_zeros)] = ret
        return ret

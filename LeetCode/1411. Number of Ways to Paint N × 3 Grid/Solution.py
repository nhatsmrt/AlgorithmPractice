class Solution:
    def numOfWays(self, n: int) -> int:
        # dp[i][j][c] = number of ways to finish the partial solution
        # at cell j of row i if previous 3 cells have color code c
        # 0 <= j <= 2; 0 <= c <= 26

        # Time and Space Complexity: O(N)

        self.n_row = n
        self.cols = [0, 1, 2]
        self.dp = {}
        self.MOD = 1000000007

        return self.complete(0, 0, 0)

    def complete(self, i: int, j: int, c: int):
        if (i, j, c) in self.dp:
            return self.dp[(i, j, c)]

        if i == self.n_row:
            return 1

        ret = 0
        if i == 0:
            forbidden_col = set()

            if j > 0:
                forbidden_col.add(self.get_color(c, j - 1))

            for new_col in self.cols:
                if new_col not in forbidden_col:
                    ret += self.complete(i + (j + 1) // 3, (j + 1) % 3, c + new_col * 3 ** j)
                    ret %= 1000000007
        else:
            prev_col = self.get_color(c, j)

            forbidden_col = {prev_col}
            if j > 0:
                forbidden_col.add(self.get_color(c, j - 1))


            for new_col in self.cols:
                if new_col not in forbidden_col:
                    ret += self.complete(i + (j + 1) // 3, (j + 1) % 3, c + (new_col - prev_col) * 3 ** j)
                    ret %= 1000000007

        self.dp[(i, j, c)] = ret
        return ret


    def get_color(self, c: int, i: int):
        if i == 0:
            return c % 3
        elif i == 1:
            return (c // 3) % 3
        else:
            return (c // 9)

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # Let dp[i][r] = maximum number of students placed in the first
        # i columns such that the (i + 1)th column has profile p
        # answer = max_{profile p} dp[len(columns)][p]

        # Time Complexity: O(m x (\sum_{i = 1}^n \binom{n}{i} 2^i))
        # = O(m 3^n)
        # Space Complexity: O(m x 2^n)

        self.col_profiles = [self.get_col_profile(seats, col) for col in range(len(seats[0]))]
        self.col_profiles.append(0)
        self.nrow = len(seats)

        self.dp = {}
        for i in range(1 << len(seats)):
            self.dp[(0, i)] = 0

        for col in range(0, len(seats[0])):
            for profile in range(0, 1 << (len(seats))):
                # col: number of cols done
                # profile: (broken) profile of (col + 1)th col
                # i.e of seats[:, col]

                if self.legal_start(profile, self.col_profiles[col]):
                    self.build(profile, profile, 0, self.col_profiles[col + 1], col + 1, 0)

        ret = 0
        for i in range(1 << len(seats)):
            ret = max(ret, self.dp.get((len(seats[0]), i), 0))

        return ret

    def build(
        self, original: int, built: int, pos: int,
        next_col_profile: int, next_col_ind: int, added: int
    ):
        if pos == self.nrow:
            self.dp[(next_col_ind, next_col_profile)] = max(
                self.dp.get((next_col_ind, next_col_profile), 0),
                self.dp.get((next_col_ind - 1, original), 0) + added
            )
        else:
            # Not place a student:
            self.build(original, built, pos + 1, next_col_profile, next_col_ind, added)

            if (built & (1 << pos)) == 0:
                # if this position is not already blocked, and try to place a student:
                built = built | (1 << pos)
                next_col_profile = next_col_profile | (1 << pos)
                if pos > 0:
                    next_col_profile = next_col_profile | (1 << (pos - 1))
                if pos < self.nrow - 1:
                    next_col_profile = next_col_profile | (1 << (pos + 1))

                self.build(original, built, pos + 1, next_col_profile, next_col_ind, added + 1)


    def get_col_profile(self, seats: List[List[str]], col: int) ->int:
        ret = 0
        for i in range(len(seats)):
            if seats[i][col] == "#":
                ret += 1 << i

        return ret

    def legal_start(self, start: int, col_profile: int):
        return start & col_profile >= col_profile

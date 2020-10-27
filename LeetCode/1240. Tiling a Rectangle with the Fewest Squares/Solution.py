from itertools import starmap


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Time Complexity: O(m^n * n^2)
        # Space Complexity: O(m^n)

        if n > m:
            return self.tilingRectangle(m, n)
        elif m == n:
            return 1

        self.cnt = 0
        terminal_state = tuple([m] * n)
        initial_state = tuple([0] * n)

        self.dp = {terminal_state: 0}
        self.n_col, self.n_row = m, n

        return self.build(initial_state)

    def build(self, state: tuple) -> int:
        if state in self.dp:
            return self.dp[state]

        start = end = 0
        ranges = []

        while end + 1 < self.n_row:
            if state[end + 1] == state[start]:
                end += 1
            else:
                ranges.append((state[start], start, end))
                start = end + 1
                end = start

        ranges.append((state[start], start,end))
        _, start, end = min(ranges)

        self.dp[state] = self.move(state, start, end)
        return self.dp[state]

    def move(self, state, start, end) -> int:
        # Time Complexity: O(n^2)
        ret = -1
        # start to end has the same indent
        max_length = min(self.n_col - state[start], end - start + 1)
        state_list = list(state)

        for i in range(1, max_length + 1):
            new_state = tuple(state_list[:start] + [state[start] + i] * i + state_list[start + i:])

            candidate = self.build(new_state)
            if candidate != -1 and (ret == -1 or ret > 1 + candidate):
                ret = 1 + candidate


        return ret

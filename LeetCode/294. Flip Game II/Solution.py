class Solution:
    def canWin(self, s: str) -> bool:
        # Time Complexity: O(2^len(s) * len(s))
        # Space Complexity: O(2^len(s))

        state = sum(1 << i for i in range(len(s)) if s[i] == "+")
        self.dp = {}
        self.str_len = len(s)
        return self.play(state)

    def play(self, state: int) -> int:
        if state in self.dp:
            return self.dp[state]

        ret = False
        for i in range(self.str_len):
            if (state & (1 << i)) and (state & (1 << (i + 1))) and not self.play(state - (1 << i) - (1 << (i + 1))):
                ret = True
                break

        self.dp[state] = ret
        return ret

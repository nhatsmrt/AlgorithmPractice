class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Time Complexity: O(2^max * max * total)
        # Space Complexity: O(2^max * total)

        if desiredTotal == 0:
            return True

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        self.dp = {}
        self.max = maxChoosableInteger
        choices = sum(1 << i for i in range(maxChoosableInteger))

        return self.play(choices, desiredTotal)

    def play(self, choices: int, remain: int):

        if (choices, remain) in self.dp:
            return self.dp[(choices, remain)]

        if remain <= 0:
            return False

        ret = False
        for i in range(0, self.max):
            if (choices & (1 << i) > 0) and not \
            self.play(choices -  (1 << i), remain - i - 1):
                ret = True
                break

        self.dp[(choices, remain)] = ret
        return ret

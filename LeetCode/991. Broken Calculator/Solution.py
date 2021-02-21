class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        # Idea: work backwards from Y to X

        # When Y is not divisible by 2, can only add 1 to it
        # When Y is divisible by 2, if Y < X, increment
        # otherwise, divide by 2

        ret = 0

        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y //= 2
            ret += 1

        return ret + X - Y

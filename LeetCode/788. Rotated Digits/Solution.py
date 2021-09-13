def to_digits(num):
    ret = []

    while num > 0:
        ret.append(num % 10)
        num //= 10

    return ret[::-1]


class Solution:
    _choices = [0, 1, 2, 5, 6, 8, 9]
    _good = {2, 5, 6, 9}

    def rotatedDigits(self, N: int) -> int:
        # Time and Space Complexity: O(W) = O(log N)
        self.digits = to_digits(N)
        self.dp = {}
        return self.build(0, False, False, False)

    def build(self, pos: int, less: bool, started: bool, good: bool) -> int:
        if (pos, less, started, good) in self.dp:
            return self.dp[(pos, less, started, good)]

        if pos == len(self.digits):
            if started and good:
                ret = 1
            else:
                ret = 0
        else:
            ret = 0

            for choice in self._choices:
                if less or choice <= self.digits[pos]:
                    ret += self.build(
                        pos + 1,
                        less or choice < self.digits[pos],
                        started or choice > 0,
                        good or choice in self._good
                    )

        self.dp[(pos, less, started, good)] = ret
        return ret

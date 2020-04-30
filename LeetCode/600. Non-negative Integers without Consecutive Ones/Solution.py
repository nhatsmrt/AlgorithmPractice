class Solution:
    def findIntegers(self, num: int) -> int:
        # Time and Space Complexity: O(log N)

        bounds = []

        while num > 0:
            bounds.append(num % 2)
            num //= 2


        self.bounds = bounds[::-1]
        self.dp = {}

        return self.build(0, 0, False)

    def build(self, pos: int, prev: int, less: bool) -> int:
        if (pos, prev, less) in self.dp:
            return self.dp[(pos, prev, less)]

        if pos == len(self.bounds):
            return 1

        ret = 0
        if less:
            ret = self.build(pos + 1, 0, True)
            if prev == 0:
                ret += self.build(pos + 1, 1, True)
        else:
            if prev == 1:
                ret = self.build(pos + 1, 0, self.bounds[pos] == 1)
            else:
                # prev = 0 = self.bounds[pos - 1]
                if self.bounds[pos] == 0:
                    ret = self.build(pos + 1, 0, False)
                else:
                    ret = self.build(pos + 1, 0, True) + self.build(pos + 1, 1, False)

        self.dp[(pos, prev, less)] = ret
        return ret

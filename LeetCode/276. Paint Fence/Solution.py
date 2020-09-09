class Solution:
    def numWays(self, n: int, k: int) -> int:
        # Time and Space Complexity: O(N)

        if not n:
            return 0

        # numways(0, same) = 1
        # numways(i, True) = (k - 1) * numways(i - 1, False)
        # numways(i, False) = (k - 1) * numways(i - 1, False) + numways(i - 1, True)

        self.dp = {}
        self.k = k

        self.count(n, False)

        return k * self.count(n - 1, False)

    def count(self, remaining: int, same: bool) -> int:
        if (remaining, same) in self.dp:
            return self.dp[(remaining, same)]

        if not remaining:
            ret = 1
        else:
            ret = self.count(remaining - 1, False) * (self.k - 1)

            if not same:
                ret += self.count(remaining - 1, True)

        self.dp[(remaining, same)] = ret
        return ret
        

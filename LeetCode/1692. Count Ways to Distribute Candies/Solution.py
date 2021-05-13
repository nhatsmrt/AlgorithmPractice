class Solution:
    _MOD = 1000000007

    def waysToDistribute(self, n: int, k: int) -> int:
        # Time Complexity: O(nk + log MOD)
        # Space Complexity: O(nk)

        self.dp = {}
        return (self.count(n, k, k) * self.inv(self.factorial(k))) % self._MOD

    def factorial(self, n):
        ret = 1
        for i in range(1, n + 1):
            ret *= i
            ret %= self._MOD

        return ret

    def inv(self, n):
        ret = 1

        power = self._MOD - 2
        i = 1
        powered = n

        while i <= power:
            if power & i > 0:
                ret *= powered
                ret %= self._MOD

            i *= 2
            powered *= powered
            powered %= self._MOD

        return ret

    def count(self, numCandies, numEmpty, k) -> int:
        key = (numCandies, numEmpty)
        numFilled = k - numEmpty

        if key in self.dp:
            return self.dp[key]

        if numCandies == numEmpty:
            ret = self.factorial(numCandies)
        else:
            ret = 0
            if numEmpty > 0:
                ret += numEmpty * self.count(numCandies - 1, numEmpty - 1, k)
                ret %= self._MOD

            if numFilled > 0:
                ret += numFilled * self.count(numCandies - 1, numEmpty, k)
                ret %= self._MOD


        self.dp[key] = ret
        return ret

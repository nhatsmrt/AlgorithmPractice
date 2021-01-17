class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Time and Space Complexity: O(N)
        self.dp = {}
        return self.count(n, 0)

    def count(self, n: int, lowest: int) -> int:
        if not n:
            return 1
        else:
            if (n, lowest) in self.dp:
                return self.dp[(n, lowest)]
            ret = 0

            for i in range(lowest, 5):
                ret += self.count(n - 1, i)

            self.dp[(n, lowest)] = ret
            return ret

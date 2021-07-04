class Solution:
    _MOD = 1000000007

    def countVowelPermutation(self, n: int) -> int:
        # Time and Space Complexity: O(N)

        self.options = {
            "$": "aeiou",
            "a": "e",
            "e": "ai",
            "i": "aeou",
            "o": "iu",
            "u": "a"
        }

        self.dp = {}
        return self.countSolutions(n, "$")

    def countSolutions(self, remain: int, prev: str) -> int:
        if (remain, prev) in self.dp:
            return self.dp[(remain, prev)]

        if remain == 0:
            return 1

        ret = 0
        for option in self.options[prev]:
            ret += self.countSolutions(remain - 1, option)
            ret %= self._MOD

        self.dp[(remain, prev)] = ret
        return ret

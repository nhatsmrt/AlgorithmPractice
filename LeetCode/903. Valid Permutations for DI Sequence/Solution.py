class Solution:
    _MOD = 1000000007

    def numPermsDISequence(self, S: str) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N^2)

        # dp[i, j] = number of permutations of 1 to (j - i + 2)
        # satisfying S[i: j + 1]
        # dp[i, j] = 1, if i >= j
        # dp[i, j] = 1[S[i] == "D"] * dp[i + 1, j] + 1[S[j] == "I"] dp[i, j - 1]
        # + sum_{k = i to j} 1[dp[k, k + 2] == "ID"] dp[i, k - 1] * dp[k + 2, j] * (end - start + 1 choose k - i - 1)
        self.dp = {}

        return self.numPermutations(S, 0, len(S) - 1)



    def numPermutations(self, S: str, start: int, end: int) -> int:
        key = (start, end)
        if key in self.dp:
            return self.dp[key]

        if start >= end:
            ret = 1
        else:
            ret = 0

            if S[start] == "D":
                ret += self.numPermutations(S, start + 1, end)

            if S[end] ==  "I":
                ret += self.numPermutations(S, start, end - 1)
                ret %= self._MOD

            binom_coeff = end - start + 1

            for peak_ind in range(start, end):
                if S[peak_ind:peak_ind + 2] == "ID":
                    left = self.numPermutations(S, start, peak_ind - 1)
                    right = self.numPermutations(S, peak_ind + 2, end)


                    num_ways = left * right
                    num_ways %= self._MOD
                    num_ways *= binom_coeff
                    num_ways %= self._MOD

                    ret += num_ways
                    ret %= self._MOD

                binom_coeff *= (end - peak_ind)
                binom_coeff //= (peak_ind - start + 2)

        self.dp[key] = ret
        return ret

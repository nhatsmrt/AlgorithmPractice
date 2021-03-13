class Solution:
    _MOD = 1000000007
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)

        # Let dp[i] = #of trees with arr[i] at root
        # dp[i] = \prod_{i1, i2: arr[i1] * arr[i2] = arr[i]} dp[i1] * dp[i2]

        self.index = {arr[i]: i for i in range(len(arr))}
        self.dp = [0] * len(arr)

        ret = 0
        for i in range(len(arr)):
            ret += self.numTreeAt(arr, i)
            ret %= self._MOD
        return ret

    def numTreeAt(self, arr: List[int], i: int) -> int:
        if self.dp[i]:
            return self.dp[i]

        ret = 1
        for factor in self.index:
            if factor < arr[i] and arr[i] % factor == 0 and arr[i] // factor in self.index:
                ind1, ind2 = self.index[factor], self.index[arr[i] // factor]
                ret += self.numTreeAt(arr, ind1) * self.numTreeAt(arr, ind2)
                ret %= self._MOD

        self.dp[i] = ret
        return ret

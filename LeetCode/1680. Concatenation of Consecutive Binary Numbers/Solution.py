class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = 1
        num_dig = 1
        MOD = 1000000007

        for i in range(2, n + 1):
            if not (i & (i - 1)):
                # i is a power of 2
                num_dig += 1

            ret = (ret << num_dig) | i
            ret %= MOD

        return ret

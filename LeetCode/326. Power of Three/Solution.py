class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        cur = 1

        while cur < n:
            cur *= 3

        return cur == n

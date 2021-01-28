class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # Time and Space Complexity: O(N)
        ret = []

        for i in range(n):
            max_remain = (n - i - 1) * 26
            choice = max(1, k - max_remain)
            k -= choice

            ret.append(chr(ord('a') + choice - 1))

        return "".join(ret)

class Solution:
    def maxPower(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = 0
        start = 0
        end = 0

        while start < len(s):
            if end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
            else:
                ret = max(ret, end - start + 1)
                start = end + 1
                end += 1

        return ret

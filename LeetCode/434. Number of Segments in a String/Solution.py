class Solution:
    def countSegments(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start, end, ret = 0, 0, 0

        while start < len(s):
            if s[start] == " ":
                start += 1
                end = start
            elif end + 1 < len(s) and s[end + 1] != " ":
                end += 1
            else:
                ret += 1
                start = end + 1
                end = start

        return ret

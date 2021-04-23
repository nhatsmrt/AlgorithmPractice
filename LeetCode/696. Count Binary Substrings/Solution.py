class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = 0
        start = 0
        end = 0

        previous = None

        while start < len(s):
            if end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
            else:
                if previous is not None:
                    ret += min(previous, end - start + 1)

                previous = end - start + 1
                end += 1
                start = end

        return ret

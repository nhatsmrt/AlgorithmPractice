class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Time and Space Complexity: O(N)

        if not s:
            return 0
        elif s == "".join(reversed(s)):
            return 1
        else:
            return 2

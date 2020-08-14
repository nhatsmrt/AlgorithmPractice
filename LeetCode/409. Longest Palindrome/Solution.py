class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Time and Space Complexity: O(N)

        counter = collections.Counter()

        for char in s:
            counter[char] += 1

        ret = 0
        for char in counter:
            if counter[char] % 2 == 0:
                ret += counter[char]
            else:
                ret += counter[char] - 1

        if ret < len(s):
            ret += 1

        return ret

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time and Space Complexity: O(N)

        lps = [0]

        for i in range(1, len(s)):
            end = lps[-1]

            while s[end] != s[i] and end > 0:
                end = lps[end - 1]

            if s[end] == s[i]:
                lps.append(end + 1)
            else:
                lps.append(0)

        return lps[-1] and not (len(s) % (len(s) - lps[-1]))

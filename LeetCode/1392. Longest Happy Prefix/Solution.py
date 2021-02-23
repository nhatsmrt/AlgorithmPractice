class Solution:
    def longestPrefix(self, s: str) -> str:
        # Let lps[i] = longest proper prefix that is also a suffix of s[:i]
        # lps[0] = lps[1] = 0
        # lps[len(s)] is the answer

        # Time and Space Complexity: O(N)
        # The value of lps increase by at most N
        # in total, and never decrease below 0
        # (i.e total number of decreases <= total number of increases)

        lps = [0, 0]
        for i in range(2, len(s) + 1):
            # Computing lps[i]:
            # We check all the prefix of s[:i - 1]
            # that is also a suffix
            # (first such prefix is s[:lps[j]])

            # For each such prefix, say s[:k], if
            # s[k] == s[i - 1], then we found the prefix that is also
            # a suffix of s[:i] (by concatenating s[k] to the end)

            # Otherwise, the next longest candidate prefix of s[:i - 1]
            # is given by lps[k]: it is the longest prefix of s[:k] that is also
            # a suffix, so it is also a prefix-suffix of s[:i - 1]

            j = i - 1
            last_char = s[i - 1]

            while j > 0 and last_char != s[lps[j]]:
                j = lps[j]

            if last_char == s[lps[j]]:
                # s[:lps[j] + 1] == s[...:i]
                lps.append(lps[j] + 1)
            else:
                lps.append(0)

        return s[:lps[-1]]

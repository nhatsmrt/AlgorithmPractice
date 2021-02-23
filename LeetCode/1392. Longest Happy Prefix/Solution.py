class Solution:
    def longestPrefix(self, s: str) -> str:
        # Let lps[i] = longest proper prefix that is also a suffix of s[:i]
        # lps[0] = lps[1] = 0
        # lps[len(s)] is the answer

        # Time and Space Complexity: O(N)
        # The value of j increase by at most N
        # in total, and never decrease below -1
        # (i.e total number of decreases + total number of increases = O(N))

        lps = [0, 0]
        j = -1

        for i in range(2, len(s) + 1):
            # Computing lps[i]:
            # We check all the prefix of s[:i - 1]
            # that is also a suffix
            # (first such prefix is s[:lps[j]])

            # For each such prefix, say s[:j], if
            # s[j] == s[i - 1], then we found the prefix that is also
            # a suffix of s[:i] (by concatenating s[j] to the end)

            # Otherwise, the next longest candidate prefix of s[:i - 1]
            # is given by lps[j]: it is the longest prefix of s[:j] that is also
            # a suffix, so it is also a prefix-suffix of s[:i - 1]

            j += 1
            last_char = s[i - 1]

            while j > 0 and last_char != s[j]:
                j = lps[j]

            if last_char == s[j]:
                # s[:j + 1] == s[...:i]
                lps.append(j + 1)
            else:
                j = -1
                lps.append(0)

        return s[:lps[-1]]

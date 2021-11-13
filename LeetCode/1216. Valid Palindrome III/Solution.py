class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Time and Space Complexity: O(N^2)

        last_occs = []

        for i, char in enumerate(s):
            if not i:
                last_occs.append({})
            else:
                last_occs.append(deepcopy(last_occs[-1]))

            last_occs[-1][char] = i


        self.last_occs = last_occs
        self.dp = {}

        return self.longestPalindrome(s, 0, len(s) - 1) >= len(s) - k

    def longestPalindrome(self, s, start, end):
        if (start, end) in self.dp:
            return self.dp[(start, end)]

        if start > end:
            return 0

        if start == end:
            return 1

        # case 1: does not select s[start]
        ret = self.longestPalindrome(s, start + 1, end)

        match = self.last_occs[end].get(s[start])
        # case 2a: s[start] has a match
        if match is not None and match > start:
            ret = max(ret, 2 + self.longestPalindrome(s, start + 1, match - 1))
        else: # s[start] does not have a match
            ret = max(ret, 1)

        self.dp[(start, end)] = ret
        return ret

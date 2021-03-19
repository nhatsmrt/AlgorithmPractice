class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        # Equivalent to finding the longest balanced string
        # This can be done as follows:
        # for each index i, find number of a's before it, and number of b's after it
        # and sum them up, then find the max over i

        a_cnt = 0
        for i in range(len(s)):
            if s[i] == "a":
                a_cnt += 1

        b_cnt = 0
        ret = 0

        for i in range(len(s) - 1, -1, -1):
            ret = max(ret, a_cnt + b_cnt)
            if s[i] == "a":
                a_cnt -= 1
            else:
                b_cnt += 1

        ret = max(ret, a_cnt + b_cnt)
        return len(s) - ret

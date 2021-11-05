class Solution:
    def maxDepth(self, s: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = 0
        num_open = 0

        for char in s:
            if char == "(":
                num_open += 1
            elif char == ")":
                num_open -= 1

            ret = max(ret, num_open)

        return ret

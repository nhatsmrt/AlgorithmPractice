class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        opening = 0
        ret = 0

        for paren in S:
            if paren == "(":
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    ret += 1

        return ret + opening

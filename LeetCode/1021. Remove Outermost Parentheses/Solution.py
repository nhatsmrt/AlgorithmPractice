class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Time and Space Complexity: O(N)
        primitive_ends = []

        opening = 0

        for i, char in enumerate(s):
            if char == "(":
                opening += 1
            else:
                opening -= 1

            if opening == 0:
                primitive_ends.append(i)

        ret = []
        start = 0

        for primitive_end in primitive_ends:
            ret.append(s[start + 1:primitive_end])
            start = primitive_end + 1

        return "".join(ret)

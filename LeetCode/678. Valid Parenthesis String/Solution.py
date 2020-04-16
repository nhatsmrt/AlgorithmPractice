class Solution:
    def checkValidString(self, s: str) -> bool:
        # Keep track of the range of the number of available openings

        low, high = 0, 0

        for char in s:
            if char == "(":
                low += 1
                high += 1

            elif char == "*":
                high += 1
                low -= 1
            else:
                low -= 1
                high -= 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0

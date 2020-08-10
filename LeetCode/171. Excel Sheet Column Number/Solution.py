class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0

        for char in s:
            ret = ret * 26 + 1 + ord(char) - ord("A")

        return ret

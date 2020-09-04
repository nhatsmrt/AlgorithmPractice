class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(self.reverse, s.split(" ")))

    def reverse(self, s: str) -> str:
        return s[::-1]

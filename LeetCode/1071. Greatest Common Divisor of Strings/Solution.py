class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Time and Space Complexity: O(N^3)
        for i in range(min(len(str1), len(str2)), -1, -1):
            prefix = str1[:i]
            if self.is_repeat(prefix, str1) and self.is_repeat(prefix, str2):
                return prefix


    def is_repeat(self, prefix, string):
        if not prefix:
            return True

        if len(string) % len(prefix):
            return False

        for i in range(0, len(string), len(prefix)):
            if string[i:i + len(prefix)] != prefix:
                return False

        return True

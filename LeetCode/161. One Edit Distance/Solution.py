class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        if len(t) - len(s) > 1:
            return False

        if len(s) == len(t):
            replaced = False

            for char1, char2 in zip(s, t):
                if char1 != char2:
                    if replaced:
                        return False

                    replaced = True

            return replaced

        offset = 0
        i = 0
        while i < len(s):
            if s[i] != t[i + offset]:
                if offset:
                    return False

                offset += 1
            else:
                i += 1

        return True

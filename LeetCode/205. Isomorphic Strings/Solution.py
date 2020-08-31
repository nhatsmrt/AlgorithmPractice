class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time and Space Complexity: O(N)

        bimap = Bimap()

        for i in range(len(s)):
            if not bimap.put(s[i], t[i]):
                return False

        return True


class Bimap:
    def __init__(self):
        self.forward, self.backward = {}, {}

    def put(self, first, second):
        if self.forward.get(first, second) == second and self.backward.get(second, first) == first:
            self.forward[first] = second
            self.backward[second] = first

            return True

        return False

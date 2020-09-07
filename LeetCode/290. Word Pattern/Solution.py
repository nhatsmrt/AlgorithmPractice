from itertools import starmap


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        # Time and Space Complexity: O(M + N)

        words = string.split()

        if len(words) != len(pattern):
            return False

        bimap = Bimap()
        return all(starmap(bimap.insert, zip(pattern, words)))

class Bimap:
    def __init__(self):
        self.forward_map = {}
        self.backward_map = {}

    def insert(self, first, second):
        if self.can_add(first, second):
            self.forward_map[first] = second
            self.backward_map[second] = first

            return True

        return False

    def can_add(self, first, second):
        return self.forward_map.get(first, second) == second and self.backward_map.get(second, first) == first

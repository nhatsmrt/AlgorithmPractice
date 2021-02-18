import re

class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Time and Space Complexity: O(N)

        words = list(filter(lambda w: len(w), re.split("\s+", text)))
        num_chars = sum(map(len, words))
        num_spaces = len(text) - num_chars
        if len(words) == 1:
            return " ".join(words) + " " * num_spaces

        num_spaces_per_words = num_spaces // (len(words) - 1)
        return (" " * num_spaces_per_words).join(words) + " " * (num_spaces - num_spaces_per_words * (len(words) - 1))

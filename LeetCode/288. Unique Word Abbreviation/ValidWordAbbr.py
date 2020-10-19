class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviated = {}

        for word, abbr in map(ValidWordAbbr.abbreviate, dictionary):
            if abbr not in self.abbreviated:
                self.abbreviated[abbr] = set()
            self.abbreviated[abbr].add(word)

    @staticmethod
    def abbreviate(word):
        if len(word) <= 2:
            return word, word

        return word, word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        # Time Complexity: O(1)

        word, abbr = ValidWordAbbr.abbreviate(word)
        return set([word]) == self.abbreviated.get(abbr, set([word]))


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

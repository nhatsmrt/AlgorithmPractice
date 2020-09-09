class Solution:
    def removeVowels(self, S: str) -> str:
        return "".join(filter(lambda c: c not in set(["a", "e", "i", "o", "u"]), S))

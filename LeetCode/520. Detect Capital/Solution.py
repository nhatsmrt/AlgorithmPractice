class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.is_lower(word) or self.is_upper(word) or (self.is_upper(word[0]) and self.is_lower(word[1:]))

    def is_lower(self, word: str):
        return word.lower() == word

    def is_upper(self, word: str):
        return word.upper() == word
        

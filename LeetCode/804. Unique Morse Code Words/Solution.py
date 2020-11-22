class Solution:
    MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time and Space Complexity: O(num_char)

        def char_to_ind(c):
            return ord(c) - ord('a')

        def word_to_morse(word):
            return "".join(map(lambda c: self.MORSE[char_to_ind(c)], word))

        return len(set(map(word_to_morse, words)))

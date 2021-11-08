class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Time Complexity: O(|chars| + sum(|word| for word in words))
        # Space Complexity: O(|chars| + max_len_word)

        cnter = Counter(chars)

        def is_good(word):
            word_cnter = Counter(word)

            for char in word_cnter:
                if cnter[char] < word_cnter[char]:
                    return False

            return True

        return sum(map(len, filter(is_good, words)))

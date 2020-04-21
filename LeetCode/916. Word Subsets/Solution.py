from typing import Dict
from functools import reduce, partial


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # Time Complexity: O(sum(len(A_i)) + sum(len(B_i)) + len(A) + len(B))
        # Space Complexity: O(len(A) + len(B))

        B = map(self.get_freq, B)
        test_str = reduce(self.combine_freq, B)

        return list(filter(partial(self.is_universal, test_str=test_str), A))

    def get_freq(self, word: str) -> List[int]:
        ret = [0] * 26
        for char in word:
            ret[ord(char) - ord('a')] += 1

        return ret

    def combine_freq(self, freqs1: List[int], freqs2: List[int]) -> List[int]:
        return [max(freq1, freq2) for freq1, freq2 in zip(freqs1, freqs2)]

    def is_universal(self, word: str, test_str: List[int]) -> bool:
        word_freq = self.get_freq(word)

        for i in range(26):
            if word_freq[i] < test_str[i]:
                return False

        return True

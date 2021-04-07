class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Time and Space Complexity: O(N)
        s = s.lower()

        lower_half = Counter(s[:len(s) // 2])
        upper_half = Counter(s[len(s) // 2:])

        def get_vowel_cnt(counter):
            return sum([counter[char] for char in "aeiou"])

        return get_vowel_cnt(lower_half) == get_vowel_cnt(upper_half)

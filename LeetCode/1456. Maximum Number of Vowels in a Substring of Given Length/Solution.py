class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        def is_vowel(char):
            return char in "aeiou"


        ret = 0
        for i in range(k):
            ret += int(is_vowel(s[i]))
        cur = ret

        for end in range(k, len(s)):
            cur += int(is_vowel(s[end])) - int(is_vowel(s[end - k]))
            ret = max(ret, cur)

        return ret

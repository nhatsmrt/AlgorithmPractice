class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        index = [-1] * 26
        for i, char in enumerate(keyboard):
            index[ord(char) - ord('a')] = i

        ret = index[ord(word[0]) - ord('a')]
        for i in range(1, len(word)):
            ret += abs(index[ord(word[i]) - ord('a')] - index[ord(word[i - 1]) - ord('a')])

        return ret

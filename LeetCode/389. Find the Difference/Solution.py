class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def compute_freq(s: str) -> List[int]:
            ret = [0] * 26

            for char in s:
                ret[ord(char) - ord('a')] += 1

            return ret

        freq_s, freq_t = compute_freq(s), compute_freq(t)

        for i in range(26):
            if freq_t[i] - freq_s[i] == 1:
                return chr(i + ord('a'))

        return -1

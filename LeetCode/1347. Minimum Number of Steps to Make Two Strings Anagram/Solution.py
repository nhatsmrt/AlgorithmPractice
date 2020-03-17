class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hist1 = self.build_freq_dict(s)
        hist2 = self.build_freq_dict(t)

        return self.diff(hist1, hist2)

    def build_freq_dict(self, s: str):
        ret = [0] * 26
        for char in s:
            ret[ord(char) - ord('a')] += 1

        return ret

    def diff(self, hist1, hist2):
        ret = 0
        for i in range(26):
            ret += abs(hist1[i] - hist2[i])
        return ret // 2

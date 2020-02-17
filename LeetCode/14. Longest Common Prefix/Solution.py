class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        lengths = [len(str) for str in strs]
        while len(strs) > 1:
            new_strings = []
            new_lengths = []

            for i in range(0, len(strs) - 1, 2):
                new_lengths.append(self.lcp2(
                    strs[i], strs[i + 1],
                    lengths[i], lengths[i + 1]
                ))
                new_strings.append(strs[i])

            if len(strs) % 2 == 1:
                new_strings.append(strs[-1])
                new_lengths.append(lengths[-1])

            strs = new_strings
            lengths = new_lengths

        return strs[0][:lengths[0]]

    def lcp2(self, str1: str, str2: str, len1: int, len2: int) -> int:
        i = 0
        bound = min([len1, len2])
        while i < bound and str1[i] == str2[i]:
            i += 1
        return i

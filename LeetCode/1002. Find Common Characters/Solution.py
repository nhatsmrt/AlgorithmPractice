class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        char_cnts = list(map(self.char_cnt, A))

        ret = []
        for i in range(26):
            cnt = min([char_cnts[j][i] for j in range(len(A))])

            for _ in range(cnt):
                ret.append(chr(i + ord('a')))

        return ret

    def char_cnt(self, string: str) -> List[int]:
        ret = [0] * 26

        for char in string:
            ret[ord(char) - ord('a')] += 1

        return ret

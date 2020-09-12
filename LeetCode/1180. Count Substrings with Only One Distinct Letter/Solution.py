class Solution:
    def countLetters(self, S: str) -> int:
        index = {}

        for i in range(len(S)):
            if S[i] not in index:
                index[S[i]] = []

            index[S[i]].append(i)

        ret = 0
        for char in index:
            ret += self.count(index[char])

        return ret

    def count(self, occs: List[int]) -> int:
        start = 0
        end = 0
        ret = 0

        while start < len(occs):
            if end + 1 < len(occs) and occs[end + 1] == occs[end] + 1:
                end += 1
            else:
                num_char = end - start + 1
                ret += num_char * (num_char + 1) // 2
                start = end + 1
                end += 1

        return ret

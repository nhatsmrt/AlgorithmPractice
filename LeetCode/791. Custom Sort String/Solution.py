class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt = [0] * len(S)
        others = []
        inverted_index = {S[i]: i for i in range(len(S))}

        for char in T:
            if char in inverted_index:
                cnt[inverted_index[char]] += 1
            else:
                others.append(char)

        ret = []
        for i in range(len(S)):
            for j in range(cnt[i]):
                ret.append(S[i])

        for char in others:
            ret.append(char)

        return ''.join(ret)

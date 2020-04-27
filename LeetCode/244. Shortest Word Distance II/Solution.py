class WordDistance:
    def __init__(self, words: List[str]):
        # Time Complexity: <O(N), O(N)>
        # Space Complexity: O(N)

        self.index = {}
        for i in range(len(words)):
            word = words[i]

            if word not in self.index:
                self.index[word] = []

            self.index[word].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        occ1 = self.index[word1]
        occ2 = self.index[word2]

        # merge sorted lists
        merged = []
        i = j = 0
        while i < len(occ1) and j < len(occ2):
            if occ1[i] < occ2[j]:
                merged.append((occ1[i], 1))
                i += 1
            else:
                merged.append((occ2[j], 2))
                j += 1

        while i < len(occ1):
            merged.append((occ1[i], 1))
            i += 1

        while j < len(occ2):
            merged.append((occ2[j], 2))
            j += 1

        ret = 100000000
        for k in range(len(merged) - 1):
            if merged[k][1] != merged[k + 1][1]:
                ret = min(ret, abs(merged[k][0] - merged[k + 1][0]))

        return ret


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

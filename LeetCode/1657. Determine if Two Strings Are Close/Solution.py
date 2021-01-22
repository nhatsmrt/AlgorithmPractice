class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time and Space Complexity: O(N)

        cnter1 = Counter(word1)
        cnter2 = Counter(word2)

        return set([k for k in cnter1]) == set([k for k in cnter2]) and self.get_cnt_of_cnt(cnter1) == self.get_cnt_of_cnt(cnter2)

    def get_cnt_of_cnt(self, cnter):
        ret = Counter()

        for key in cnter:
            ret[cnter[key]] += 1

        return ret

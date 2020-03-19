class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # Time Complexity: O(|S| + sum(|word_i|))
        # Space Complexity: O(|S|)

        self.to_ind = lambda char: ord(char) - ord('a')

        suff_inv_ind = [[-1 for j in range(26)] for i in range(len(S) + 1)]
        for i in range(len(S) - 1, -1, -1):
            for j in range(26):
                suff_inv_ind[i][j] = suff_inv_ind[i + 1][j]
            suff_inv_ind[i][self.to_ind(S[i])] = i

        ret = 0
        for word in words:
            if self.contains(suff_inv_ind, word):
                ret += 1

        return ret

    def contains(self, suff_inv_ind: List[List[int]], word: str) -> bool:
        suff = 0
        for char in word:
            next_occ = suff_inv_ind[suff][self.to_ind(char)]
            if next_occ == -1:
                return False
            suff = next_occ + 1

        return True


        

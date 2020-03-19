class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # Time Complexity: O(|S| + sum(|d_i|))
        # Space Complexity: O(|S|)

        suffix_inv_inds = [[-1 for j in range(26)] for i in range(len(s) + 1)]

        for i in range(len(s) - 1, -1, -1):
            for j in range(26):
                suffix_inv_inds[i][j] = suffix_inv_inds[i + 1][j]
            suffix_inv_inds[i][ord(s[i]) - ord('a')] = i

        ret_str = ""

        for word in d:
            if (len(word) > len(ret_str) or (len(word) == len(ret_str) and word < ret_str)) and self.contains(suffix_inv_inds, word):
                ret_str = word

        return ret_str

    def contains(self, suffix_inv_inds: List[List[int]], word: str) -> bool:
        cur = 0
        for i in range(len(word)):
            if suffix_inv_inds[cur][ord(word[i]) - ord('a')] == -1:
                return False
            else:
                cur = suffix_inv_inds[cur][ord(word[i]) - ord('a')] + 1

        return True

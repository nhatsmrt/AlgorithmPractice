class Bimap:
    def __init__(self):
        self.word_to_cnt = {}
        self.cnt_to_word = {}

    def add(self, word: str):
        cnt = self.word_to_cnt.get(word, 0) + 1
        if cnt not in self.cnt_to_word:
            self.cnt_to_word[cnt] = set()

        self.word_to_cnt[word] = cnt
        self.cnt_to_word[cnt].add(word)

        if cnt > 1:
            self.cnt_to_word[cnt - 1].remove(word)

    def get_most_cnt(self, k: int) -> List[str]:
        words = [(word, self.word_to_cnt[word]) for word in self.word_to_cnt]
        ret = []

        # Make Heap: O(N)
        for j in range(len(words) // 2, -1, -1):
            self.percolate_down(words, j)

        for i in range(k):
            # Remove root: O(log N)
            tmp = words[0]
            words[0] = words[-1]
            words[-1] = tmp
            ret.append(words.pop()[0])
            self.percolate_down(words, 0)
        return ret

    def percolate_down(self, words, j):
        if j * 2 + 1 < len(words):
            swap_ind = self.get_min_inds(words, j, j * 2 + 1)
            if j * 2 + 2 < len(words):
                swap_ind = self.get_min_inds(words, swap_ind, j * 2 + 2)

            if swap_ind != j:
                tmp = words[j]
                words[j] = words[swap_ind]
                words[swap_ind] = tmp
                self.percolate_down(words, swap_ind)


    def get_min_inds(self, words, i, j):
        word1, cnt1 = words[i]
        word2, cnt2 = words[j]
        if cnt1 > cnt2 or (cnt1 == cnt2 and word1 < word2):
            return i

        return j

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Time Complexity: O(N + k log N)
        # Space Complexity: O(N)
        bimap = Bimap()
        for word in words:
            bimap.add(word)
        return bimap.get_most_cnt(k)

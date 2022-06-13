class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word_cnter: List[int]):
        it = self.root

        for cnt in word_cnter:
            if not it.children.get(cnt):
                it.children[cnt] = TrieNode()

            it = it.children[cnt]

        it.is_word = True

    def contains(self, word_cnter: List[int]) -> bool:
        it = self.root

        for cnt in word_cnter:
            if not it.children.get(cnt):
                return False

            it = it.children[cnt]

        return it.is_word



class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # Time Complexity: O(|startWords| + |targetWords| + Wstart + sum_{word in targetWords} |word|^2) = O(|startWords| + |targetWords|)
        # Space Complexity: O(Wstart + Wtarget) = O(|startWords| + |targetWords|)

        # where Wstart, Wtarget are the total number of characters in start words and target words, respectively.
        # note that the length of each word in either list is upper-bounded by 26 = O(1)

        def char_to_ind(char: str) -> int:
            return ord(char) - ord('a')

        @lru_cache
        def word_to_cnter(word: str) -> List[int]:
            index = [0] * 26

            for char in word:
                index[char_to_ind(char)] += 1

            ret = []

            for i, present in enumerate(index):
                if present:
                    ret.append(i)

            return ret

        cnters = {}
        start_trie = Trie()
        target_trie = Trie()

        for start in startWords:
            cnters[start] = word_to_cnter(start)
            start_trie.insert(cnters[start])

        for target in targetWords:
            cnters[target] = word_to_cnter(target)
            target_trie.insert(cnters[target])

        ret = 0
        for target in targetWords:
            target_cnter = cnters[target]

            if len(target_cnter) > 1:
                for i in range(len(target_cnter)):
                    candidate = target_cnter[:i] + target_cnter[i + 1:]

                    if start_trie.contains(candidate):
                        ret += 1
                        break

        return ret

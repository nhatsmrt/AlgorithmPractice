class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        it = self.root

        for char in word:
            char_ind = int(char)

            if not it.children[char_ind]:
                it.children[char_ind] = TrieNode()

            it = it.children[char_ind]

        ret = 0 if it.is_word else 1
        it.is_word = True

        return ret


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Time and Space Complexity: O(NK)

        num_binary_str = 0
        trie = Trie()

        for i in range(len(s) - k + 1):
            num_binary_str += trie.insert(s[i:i + k])

        return num_binary_str == 2 ** k

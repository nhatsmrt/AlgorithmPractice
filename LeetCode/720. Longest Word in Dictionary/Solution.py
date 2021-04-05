class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        it = self.root
        for char in word:
            if char not in it.children:
                it.children[char] = TrieNode()

            it = it.children[char]

        it.word = word

    def solve(self):
        return self.solve_from(self.root)

    def solve_from(self, node):
        ret = None

        for char in node.children:
            child = node.children[char]
            if child.word is not None:
                child_word = self.solve_from(child)

                if not ret or len(child_word) > len(ret) or len(child_word) == len(ret) and child_word < ret:
                    ret = child_word

        if not ret:
            return node.word
        return ret


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Time and Space Complexity: O(sum(len(word)))

        trie = Trie()

        for word in words:
            trie.insert(word)

        return trie.solve()

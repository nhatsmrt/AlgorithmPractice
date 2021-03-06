def get_ind(c):
    return ord(c) - ord('a')


class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        it = self.root
        for char in word:
            if not it.children[get_ind(char)]:
                it.children[get_ind(char)] = TrieNode()
            it = it.children[get_ind(char)]

        it.is_word = True

    def find_encodings(self):
        total_length, num_leaves = self.dfs(self.root, 0)
        return total_length + num_leaves

    def dfs(self, node: TrieNode, height: int):
        if len(node.children) == 0:
            return (height, 1)

        total_length = 0
        num_leaves = 0

        for child_ind in node.children:
            child = node.children[child_ind]
            child_length, child_leaves = self.dfs(child, height + 1)
            num_leaves += child_leaves
            total_length += child_length

        return (total_length, num_leaves)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Time and Space Complexity: O(sum(word_len))

        trie = Trie()
        for word in words:
            trie.insert(reversed(word))

        return trie.find_encodings()
        

class UnionFind:
    def __init__(self, words: set):
        self.words = words
        self.par = {word: word for word in words}
        self.weight = {word: 1 for word in words}

    def union(self, word1, word2):
        root1, root2 = self.find(word1), self.find(word2)

        if root1 != root2:
            # union by weight:
            if self.weight[root1] < self.weight[root2]:
                self.weight[root2] += self.weight[root1]
                self.par[root1] = root2
            else:
                self.weight[root1] += self.weight[root2]
                self.par[root2] = root1

    def find(self, word: str) -> str:
        if self.par[word] == word:
            return word

        root = self.find(self.par[word])
        self.par[word] = root  # path compression
        return root


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # Time Complexity: O((V + E) \alpha(V))
        # Space Complexity: O(V)

        if len(words1) != len(words2):
            return False

        words = set()

        for word1, word2 in zip(words1, words2):
            words.add(word1)
            words.add(word2)

        for pair in pairs:
            words.add(pair[0])
            words.add(pair[1])

        uf = UnionFind(words)

        for pair in pairs:
            uf.union(pair[0], pair[1])

        for word1, word2 in zip(words1, words2):
            if uf.find(word1) != uf.find(word2):
                return False

        return True

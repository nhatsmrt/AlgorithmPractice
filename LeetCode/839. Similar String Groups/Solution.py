class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.n_comp = n

    def union(self, num1: int, num2: int):
        root1, root2 = self.find(num1), self.find(num2)
        if root1 != root2:
            # Union by rank:
            if self.rank[root1] < self.rank[root2]:
                self.par[root1] = root2
                self.rank[root2] += self.rank[root1]
            else:
                self.par[root2] = root1
                self.rank[root1] += self.rank[root2]
            self.par[num1] = self.par[num2] = self.par[root1]
            self.n_comp -= 1

    def num_components(self) -> int:
        return self.n_comp

    def find(self, num: int) -> int:
        if self.par[num] == num:
            return num

        root = self.find(self.par[num])
        # Path Compression:
        self.par[num] = root

        return root


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        # Time Complexity: O(NW min(N, W^2))
        # Space Complexity: O(NW)
        
        A = list(set(A))

        word_len = len(A[0])
        num_words = len(A)
        self.adj_lists = None

        if word_len ** 2 <= num_words:
            self.adj_lists = [[False for j in range(num_words)] for i in range(num_words)]
            inverted_index = {A[i]: i for i in range(num_words)}
            for i in range(num_words):
                self.build_adj(A[i], i, inverted_index)

        uf = UnionFind(len(A))

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if self.is_adjacent(A, i, j):
                    uf.union(i, j)

        return uf.num_components()

    def build_adj(self, word: str, ind: int, inverted_index):
        chars = [char for char in word]

        for pos1 in range(len(word)):
            for pos2 in range(pos1 + 1, len(word)):
                if chars[pos1] != chars[pos2]:
                    self.swap(chars, pos1, pos2)
                    neighbor = ''.join(chars)
                    if neighbor in inverted_index:
                        nei_ind = inverted_index[neighbor]
                        if not self.adj_lists[ind][nei_ind]:
                            self.adj_lists[ind][nei_ind] = self.adj_lists[nei_ind][ind] = True
                    self.swap(chars, pos1, pos2)
    def swap(self, chars: List[str], pos1: int, pos2: int):
        tmp = chars[pos1]
        chars[pos1] = chars[pos2]
        chars[pos2] = tmp

    def is_adjacent(self, words: List[str], i: int, j: int) -> bool:
        if self.adj_lists is None:
            str1, str2 = words[i], words[j]

            diff = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    diff += 1
                if diff == 3:
                    return False

            return diff == 0 or diff == 2
        else:
            return self.adj_lists[i][j]

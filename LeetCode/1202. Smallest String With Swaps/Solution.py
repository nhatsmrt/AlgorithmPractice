def count_sort(chars):
    cnter = [0] * 26
    ret = []

    for char in chars:
        cnter[ord(char) - ord('a')] += 1

    for i, cnt in enumerate(cnter):
        char = chr(i + ord('a'))

        for _ in range(cnt):
            ret.append(char)

    return ret


class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.weight = [1] * n

    def find(self, node):
        if self.par[node] == node:
            return node

        ret = self.find(self.par[node])
        self.par[node] = ret
        return ret

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.par[root1] = root2
                self.weight[root2] += self.weight[root1]
            else:
                self.par[root2] = root1
                self.weight[root1] += self.weight[root2]

    def sort(self, string):
        ret = [None] * len(string)

        comp_chars = {}
        comp_inds = {}

        for i, char in enumerate(string):
            root = self.find(i)

            if root not in comp_chars:
                comp_chars[root] = []
                comp_inds[root] = []

            comp_chars[root].append(char)
            comp_inds[root].append(i)

        for root in comp_chars:
            for i, char in zip(comp_inds[root], count_sort(comp_chars[root])):
                ret[i] = char

        return "".join(ret)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Time Complexity: O(|pairs| alpha(s) + |s|)
        # Space Complexity: O(|s|)

        uf = UnionFind(len(s))

        for first, second in pairs:
            uf.union(first, second)

        return uf.sort(s)

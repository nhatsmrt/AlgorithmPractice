class UnionFind:
    def __init__(self):
        self.par = {}
        self.sizes = {}

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            if self.sizes[root1] < self.sizes[root2]:
                self.par[root1] = root2
                self.sizes[root2] += self.sizes[root1]
            else:
                self.par[root2] = root1
                self.sizes[root1] += self.sizes[root2]

    def find(self, node: int):
        if self.par[node] == node:
            return node

        root = self.find(self.par[node])
        self.par[node] = root # path compression
        return root

    def add(self, node: int):
        if node not in self.par:
            self.par[node] = node
            self.sizes[node] = 1

    def get_comp_size(self, node: int):
        if node not in self.par:
            return 0

        return self.sizes[self.find(node)]


class LUPrefix:
    # Space Complexity: O(n)
    # Time Complexity: O(m alpha(m, n)) for m queries
    # # amortized O(alpha(m, n)), roughly O(1) per query

    def __init__(self, n: int):
        self.uf = UnionFind()
        self.bound = n


    def upload(self, video: int) -> None:
        self.uf.add(video)

        if video - 1 in self.uf.par:
            self.uf.union(video, video - 1)

        if video + 1 in self.uf.par:
            self.uf.union(video, video + 1)

    def longest(self) -> int:
        return self.uf.get_comp_size(1)


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

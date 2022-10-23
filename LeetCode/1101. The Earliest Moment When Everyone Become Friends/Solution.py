class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n
        self.num_connected = n

    def find(self, node):
        if self.par[node] == node:
            return node

        self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            self.num_connected -= 1

            if self.size[root1] <= self.size[root2]:
                self.par[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.par[root2] = root1
                self.size[root1] += self.size[root2]

        return self.num_connected


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Time Complexity: O(L log L + L alpha(N, L))

        uf = UnionFind(n)

        for timestamp, per1, per2 in sorted(logs):
            if uf.union(per1, per2) == 1:
                return timestamp

        return -1

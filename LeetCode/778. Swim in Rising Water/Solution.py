class UnionFind:
    def __init__(self):
        self.par = {}
        self.weight = {}

    def add(self, node):
        if node not in self.par:
            self.par[node] = node
            self.weight[node] = 1

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return False

        if self.weight[root1] < self.weight[root2]:
            self.par[root1] = root2
            self.weight[root2] += self.weight[root1]
        else:
            self.par[root2] = root1
            self.weight[root1] += self.weight[root2]

        return True

    def find(self, node):
        if self.par.get(node, node) == node:
            return node

        ret = self.find(self.par[node])
        self.par[node] = ret  # path compression
        return ret


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(N^2 (sort(N^2) + \alpha(N^2)))
        # Space Complexity: O(N^2)

        edges = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < len(grid):
                    dist = max(grid[i][j], grid[i + 1][j])
                    edges.append((dist, (i, j), (i + 1, j)))

                if j + 1 < len(grid[0]):
                    dist = max(grid[i][j], grid[i][j + 1])
                    edges.append((dist, (i, j), (i, j + 1)))

        edges.sort()
        uf = UnionFind()

        for dist, node1, node2 in edges:
            uf.add(node1)
            uf.add(node2)

            if uf.union(node1, node2) and uf.find((0, 0)) == uf.find((len(grid) - 1, len(grid[0]) - 1)):
                return dist

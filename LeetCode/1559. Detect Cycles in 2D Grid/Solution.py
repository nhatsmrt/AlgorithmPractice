class UnionFind:
    def __init__(self):
        self.par = {}
        self.root = {}
        self.weight = {}

    def union(self, pos1, pos2):
        root1, root2 = self.find(pos1), self.find(pos2)

        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.par[root1] = root2
                self.weight[root2] += self.weight[root1]
            else:
                self.par[root2] = root1
                self.weight[root1] += self.weight[root2]

        return root1 == root2

    def find(self, pos):
        if pos not in self.par:
            self.par[pos] = pos
            self.weight[pos] = 1
            return pos

        if self.par[pos] == pos:
            return pos

        ret = self.find(self.par[pos])
        self.par[pos] = ret # path compression
        return ret

        
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Time Complexity: O(MN alpha(MN))
        # Space Complexity: O(MN)

        uf = UnionFind()

        moves = [(-1, 0), (0, -1)]

        def is_valid(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for move in moves:
                    neigh_i, neigh_j = i + move[0], j + move[1]

                    if is_valid(neigh_i, neigh_j) and grid[i][j] == grid[neigh_i][neigh_j]:
                        if uf.union((i, j), (neigh_i, neigh_j)):
                            return True

        return False

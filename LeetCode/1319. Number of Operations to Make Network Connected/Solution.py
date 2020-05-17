class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.weight = [1 for i in range(n)]


    def union(self, i: int, j: int) -> bool:
        root1, root2 = self.find(i), self.find(j)

        if root1 == root2:
            return False

        if self.weight[root1] < self.weight[root2]:
            self.par[root1] = root2
            self.weight[root2] += self.weight[root1]
        else:
            self.par[root2] = root1
            self.weight[root1] += self.weight[root2]

        return True


    def find(self, i: int):
        if i == self.par[i]:
            return i

        root = self.find(self.par[i])
        self.par[i] = root # path compression

        return root


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Modified Kruskal Algorithm
        # Time Complexity: O(N\alpha(N))
        # Space Complexity: O(N)

        if len(connections) < n - 1:
            return -1

        num_edge = 0
        uf = UnionFind(n)

        for connection in connections:
            if uf.union(connection[0], connection[1]):
                num_edge += 1

        return n - 1 - num_edge

        

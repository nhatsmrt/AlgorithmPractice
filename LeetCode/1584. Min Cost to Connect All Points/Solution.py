def l1(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [1] * n

    def union(self, i: int, j: int):
        root1, root2 = self.find(i), self.find(j)
        if root1 != root2:
            # Union by rank:
            if self.rank[root1] < self.rank[root2]:
                self.par[root1] = root2
                self.rank[root2] += self.rank[root1]
            else:
                self.par[root2] = root1
                self.rank[root1] += self.rank[root2]
            return True
        else:
            return False

    def find(self, i: int):
        if self.par[i] == i:
            return i

        root = self.find(self.par[i])
        self.par[i] = root # path compression
        return root



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time Complexity: O(N^2 log N)
        # Space Complexity: O(N^2)

        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((l1(points[i], points[j]), i, j))


        # Kruskal's Algorithm:
        uf = UnionFind(len(points))
        edges.sort()
        ret = 0

        for (dist, i, j) in edges:
            if uf.union(i, j):
                ret += dist

        return ret

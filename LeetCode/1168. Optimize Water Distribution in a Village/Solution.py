class Node:
    def __init__(self, ind: int):
        self.par = self
        self.ind = ind
        self.rank = 1


class UnionFind:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]

    def union(self, node_ind1: int, node_ind2: int) -> bool:
        node1 = self.find_root_of(self.nodes[node_ind1])
        node2 = self.find_root_of(self.nodes[node_ind2])

        if node1 != node2:
            if node1.rank < node2.rank:
                node1.par = node2
                node2.rank += node1.rank
            else:
                node2.par = node1
                node1.rank += node2.rank
            return True
        else:
            return False

    def find_root_of(self, node: Node) -> Node:
        par = node.par
        if node == par:
            return node

        root = self.find_root_of(par)
        node.par = root  # path compression
        return root


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        edges = []
        uf = UnionFind(n + 1)
        for i in range(len(wells)):
            edges.append((wells[i], 0, i + 1))

        for pipe in pipes:
            edges.append((pipe[-1], pipe[0], pipe[1]))

        heapq.heapify(edges)
        ret = 0

        while len(edges) > 0:
            edge = heapq.heappop(edges)
            if uf.union(edge[1], edge[2]):
                ret += edge[0]
        return ret
        

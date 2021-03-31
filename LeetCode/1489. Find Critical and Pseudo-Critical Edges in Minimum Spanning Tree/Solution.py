class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.weight = [1] * n

    def union(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return False

        # Union by weight:
        if self.weight[root1] < self.weight[root2]:
            self.par[root1] = root2
            self.weight[root2] += self.weight[root1]
        else:
            self.par[root2] = root1
            self.weight[root1] += self.weight[root2]

        return True


    def find(self, node: int) -> int:
        if self.par[node] == node:
            return node

        ret = self.find(self.par[node])
        self.par[node] = ret  # path compression
        return ret

    def is_connected(self) -> bool:
        for i in range(len(self.par) - 1):
            if self.find(i) != self.find(i + 1):
                return False

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(E^2 \alpha(E))

        # An edge is critical if its removal increase the MST weight
        # An edge is pseudo-critical if its (forced) inclusion does not increase MST weight

        sorted_edges = sorted(enumerate(edges), key=lambda ind_data: ind_data[1][2])
        ret = [[], []]

        mst_weight = self.kruskal(n, edges, sorted_edges)

        # Find critical edge:
        for i in range(len(edges)):
            exclusion_weight = self.kruskal(n, edges, sorted_edges, exclusion=i)
            inclusion_weight = self.kruskal(n, edges, sorted_edges, inclusion=i)

            if exclusion_weight < 0 or exclusion_weight > mst_weight:
                ret[0].append(i)

            elif inclusion_weight == mst_weight:
                ret[1].append(i)

        return ret



    def kruskal(self, n, edges, sorted_edges, exclusion=-1, inclusion=-1) -> int:
        uf = UnionFind(n)
        ret = 0

        if inclusion >= 0:
            uf.union(edges[inclusion][0], edges[inclusion][1])
            ret += edges[inclusion][2]

        for edge_ind, (from_node, to_node, weight) in sorted_edges:
            if edge_ind != inclusion and edge_ind != exclusion and uf.union(from_node, to_node):
                ret += weight

        if uf.is_connected():
            return ret
        return -1

class KRTNode:
    def __init__(self, weight: int=0, left=None, right=None):
        self.weight, self.left, self.right = weight, left, right
        self.par = None

    def __repr__(self):
        return str(self.weight)



class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.weight = [1] * n
        self.krt_leaves = [KRTNode(0) for i in range(n)]
        self.krt = [self.krt_leaves[i] for i in range(n)]

    def union(self, node1: int, node2: int, edge_weight: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return False

        # union by weight:
        if self.weight[root1] < self.weight[root2]:
            self.par[root1] = root2
            self.weight[root2] += self.weight[root1]

            self.krt[root2] = KRTNode(edge_weight, self.krt[root1], self.krt[root2])
            self.krt[root2].left.par = self.krt[root2]
            self.krt[root2].right.par = self.krt[root2]
        else:
            self.par[root2] = root1
            self.weight[root1] += self.weight[root2]

            self.krt[root1] = KRTNode(edge_weight, self.krt[root1], self.krt[root2])
            self.krt[root1].left.par = self.krt[root1]
            self.krt[root1].right.par = self.krt[root1]
        return True

    def find(self, node: int) -> int:
        if self.par[node] == node:
            return node

        ret = self.find(self.par[node])
        self.par[node] = ret  # path compression
        return ret


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        # Time Complexity: O(E log E + V log V)
        # Space Complexity: O(V log V)

        # Idea: Minimum maximum edge along all paths between two node
        # is the weight at the LCA of the two corresponding leaves
        # in the Kruskal Reconstruction Tree

        # Execute Kruskal Algorithm and build Kruskal Reconstruction Tree:
        uf = UnionFind(n)
        edgeList.sort(key=lambda edge: edge[-1])

        for node1, node2, weight in edgeList:
            uf.union(node1, node2, weight)

        # Build binary lifting tables:
        binary_lifting_tables = {}
        for i in range(n):
            krt_root = uf.krt[uf.find(i)]

            if krt_root not in binary_lifting_tables:
                binary_lifting_tables[krt_root] = self.build_binary_lifting(krt_root)

        self.uf, self.binary_lifting_tables = uf, binary_lifting_tables

    def build_binary_lifting(self, root: KRTNode):
        nodes = []
        times = {}
        self.timestamp = 0

        self.find_all_nodes(root, nodes, times)
        ret = [{node: node.par if node.par else node for node in nodes}]

        while True:
            all_root = False
            new_row = {}

            for node in nodes:
                all_root = all_root or ret[-1][node] != ret[-1][ret[-1][node]]
                new_row[node] = ret[-1][ret[-1][node]]

            if all_root:
                ret.append(new_row)
            else:
                break

        return ret, times

    def find_all_nodes(self, node, all_nodes, times):
        if node:
            start = self.timestamp
            self.timestamp += 1

            all_nodes.append(node)
            self.find_all_nodes(node.left, all_nodes, times)
            self.find_all_nodes(node.right, all_nodes, times)

            end = self.timestamp
            self.timestamp += 1
            times[node] = start, end


    def _is_ancestor(self, node1, node2, times):
        return times[node1][0] <= times[node2][0] and times[node2][1] <= times[node1][1]

    def query(self, p: int, q: int, limit: int) -> bool:
        # Time Complexity: O(log N) per query
        if self.uf.find(p) != self.uf.find(q):
            # p and q are not connected
            return False

        root = self.uf.find(p)
        bl_table, times = self.binary_lifting_tables[self.uf.krt[root]]
        leaf1, leaf2 = self.uf.krt_leaves[p], self.uf.krt_leaves[q]

        i = len(bl_table) - 1
        it = leaf1

        for i in range(len(bl_table) - 1, -1, -1):
            if not self._is_ancestor(bl_table[i][it], leaf2, times):
                it = bl_table[i][it]


        it = bl_table[0][it]
        return it.weight < limit


# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)

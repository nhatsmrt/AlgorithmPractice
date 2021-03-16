class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.weight = [1] * n

    def union(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)

        if root1 == root2:
            return False

        # union by weight:
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

    def clear(self):
        n = len(self.par)
        self.par = list(range(n))
        self.weight = [1] * n


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Time Complexity: O(((Q + M) log(N) + N) log(M))
        # Space Complexity: O(N)

        edgeList.sort(key=lambda edge: edge[-1])
        uf = UnionFind(n)

        query_max_edges = [0]
        query_search_space = [[0, len(edgeList) - 1] for _ in range(len(queries))]
        num_rounds = math.ceil(math.log2(len(edgeList)))

        for _ in range(num_rounds):
            # find midpoints of each query:
            query_midpoints = list(map(lambda space: (space[0] + space[1]) // 2, query_search_space))

            query_midpoints_index = {}
            for i, midpoint in enumerate(query_midpoints):
                if midpoint not in query_midpoints_index:
                    query_midpoints_index[midpoint] = []
                query_midpoints_index[midpoint].append(i)

            for i, edge in enumerate(edgeList):
                uf.union(edge[0], edge[1])

                for query_ind in query_midpoints_index.get(i, []):
                    node1, node2 = queries[query_ind][0], queries[query_ind][1]

                    if uf.find(node1) == uf.find(node2):
                        query_search_space[query_ind][1] = i
                    else:
                        query_search_space[query_ind][0] = i + 1

            uf.clear()

        ret = []
        for i, query in enumerate(queries):
            ans = query_search_space[i][0] == query_search_space[i][1] and edgeList[query_search_space[i][0]][-1] < query[-1]
            ret.append(ans)

        return ret

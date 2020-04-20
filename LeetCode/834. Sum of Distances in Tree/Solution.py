class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # Tree-Rerooting DP
        # Time and Spcae Complexity: O(N)

        adj_lists = [set() for i in range(N)]

        for edge in edges:
            adj_lists[edge[0]].add(edge[1])
            adj_lists[edge[1]].add(edge[0])

        self.adj_lists = adj_lists
        ret = [0] * N # ret[n] = sum of distances from n if n is root
        self.dist = [0] * N
        self.size = [1] * N
        # dist[n] = sum of distances from n to the nodes in its subtree given the current root

        self.dfs(0, None)
        ret[0] = self.dist[0]
        self.reroot(0, None, ret)

        return ret


    def dfs(self, cur: int, par: int):
        ret = 0

        for child in self.adj_lists[cur]:
            if par is None or child != par:
                self.dfs(child, cur)
                self.size[cur] += self.size[child]
                self.dist[cur] += self.dist[child] + self.size[child]


    def reroot(self, cur: int, par: int, ret: List[int]):
        for child in self.adj_lists[cur]:
            if par is None or child != par:
                # Reroot:
                self.dist[cur] -= self.dist[child] + self.size[child]
                self.size[cur] -= self.size[child]

                self.dist[child] += self.dist[cur] + self.size[cur]
                self.size[child] += self.size[cur]
                ret[child] = self.dist[child]
                # Recursion:
                self.reroot(child, cur, ret)

                # Undo rerooting:
                self.dist[child] -= self.dist[cur] + self.size[cur]
                self.size[child] -= self.size[cur]

                self.dist[cur] += self.dist[child] + self.size[child]
                self.size[cur] += self.size[child]

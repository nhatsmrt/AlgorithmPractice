class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time and Space Complexity: O(V + E)

        adj_lists = {}

        for edge in edges:
            if edge[0] not in adj_lists:
                adj_lists[edge[0]] = set()

            if edge[1] not in adj_lists:
                adj_lists[edge[1]] = set()

            adj_lists[edge[0]].add(edge[1])
            adj_lists[edge[1]].add(edge[0])


        ret = 0
        unvisited = set([i for i in range(n)])
        while len(unvisited) > 0:
            ret += 1
            node = unvisited.pop()
            self.dfs(node, adj_lists, unvisited)

        return ret

    def dfs(self, node: int, adj_lists: dict, unvisited: set):
        for neigh in adj_lists.get(node, []):
            if neigh in unvisited:
                unvisited.remove(neigh)
                self.dfs(neigh, adj_lists, unvisited)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Time and Space Complexity: O(V + E)

        adj_lists = {i: set() for i in range(n)}

        for edge in connections:
            adj_lists[edge[0]].add((edge[1], 1))
            adj_lists[edge[1]].add((edge[0], 0))

        return self.dfs(0, adj_lists, set())

    def dfs(self, node, adj_lists, visited) -> int:
        ret = 0
        visited.add(node)

        for neighbor, direction in adj_lists[node]:
            if neighbor not in visited:
                if direction: ret += 1
                ret += self.dfs(neighbor, adj_lists, visited)

        return ret

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Time and Space Complexity: O(V + E)

        self.safe = set()
        visited = set()

        for node in range(len(graph)):
            if node not in visited:
                self.dfs(node, graph, visited)

        return list(filter(lambda node: node in self.safe, range(len(graph))))

    def dfs(self, node, graph, visited) -> bool:
        visited.add(node)
        ret = True

        if graph[node]:  # non-terminal node
            for neighbor in graph[node]:
                if neighbor in visited:
                    ret = ret and neighbor in self.safe
                else:
                    ret = ret and self.dfs(neighbor, graph, visited)

        if ret:
            self.safe.add(node)

        return ret

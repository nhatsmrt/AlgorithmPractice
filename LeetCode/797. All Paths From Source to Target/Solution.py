class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Time and Space Complexity: O(N 2^N)

        ret = []
        self.dfs(graph, 0, [0], ret)

        return ret

    def dfs(self, graph: List[List[int]], node: int, path: List[int], ret: List[List[int]]):
        if node == len(graph) - 1:
            ret.append(path.copy())
        else:
            for neighbor in graph[node]:
                path.append(neighbor)
                self.dfs(graph, neighbor, path, ret)
                path.pop()
        

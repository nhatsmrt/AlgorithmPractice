class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Time and Space Complexity: O(V + E)

        adj_list = {i: room for i, room in enumerate(rooms)}

        visited = set()
        self.dfs(0, visited, adj_list)
        return len(visited) == len(rooms)

    def dfs(self, node, visited, adj_list):
        visited.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, adj_list)

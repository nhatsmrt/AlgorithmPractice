class Solution:
    MOVE = {
        1: [(0, 1), (0, -1)],
        2: [(1, 0), (-1, 0)],
        3: [(0, -1), (1, 0)],
        4: [(1, 0), (0, 1)],
        5: [(-1, 0), (0, -1)],
        6: [(-1, 0), (0, 1)]
    }

    def is_valid(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Time and Space Complexity: O(MN)

        adj_lists = {(i, j): set() for i in range(len(grid)) for j in range(len(grid[0]))}

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                for move in self.MOVE[grid[i][j]]:
                    new_pos = i + move[0], j + move[1]

                    if self.is_valid(grid, new_pos[0], new_pos[1]):
                        adj_lists[(i, j)].add(new_pos)
        self.adj_lists = adj_lists

        return self.dfs((0, 0), grid, set())

    def dfs(self, pos, grid, visited):
        if pos == (len(grid) - 1, len(grid[0]) - 1):
            return True

        visited.add(pos)

        for neighbor in self.adj_lists[pos]:
            if neighbor not in visited and pos in self.adj_lists[neighbor] and self.dfs(neighbor, grid, visited):
                return True

        return False

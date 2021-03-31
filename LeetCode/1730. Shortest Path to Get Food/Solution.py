class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(MN)
        # Space Complexity: O(M + N)

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        traverse = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    traverse.append((0, (i, j)))
                    visited.add((i, j))

                if traverse:
                    break

            if traverse:
                break

        while traverse:
            dist, (i, j) = traverse.popleft()

            if grid[i][j] == "#":
                return dist

            for move in moves:
                new_i, new_j = i + move[0], j + move[1]

                if (new_i, new_j) not in visited and new_i >= 0 and new_j >= 0 and new_i < len(grid) and new_j < len(grid[0]) and grid[new_i][new_j] != "X":
                    visited.add((new_i, new_j))
                    traverse.append((dist + 1, (new_i, new_j)))

        return -1

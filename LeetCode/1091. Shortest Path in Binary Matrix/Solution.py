class Solution:
    MOVES = [
        (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        if grid[0][0] or grid[-1][-1]:
            return -1

        adj_lists = {}

        def is_valid(pos):
            return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0]) and not grid[pos[0]][pos[1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    adj_lists[(i, j)] = set()

                    for move in self.MOVES:
                        new_i, new_j = i + move[0], j + move[1]

                        if is_valid((new_i, new_j)):
                            adj_lists[(i, j)].add((new_i, new_j))


        traverse_queue = deque()
        visited = set([(0, 0)])
        traverse_queue.append(((0, 0), 1))

        while traverse_queue:
            pos, dist = traverse_queue.popleft()

            if pos == (len(grid) - 1, len(grid[0]) - 1):
                return dist

            for neighbor in adj_lists[pos]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    traverse_queue.append((neighbor, dist + 1))

        return -1

from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # Complexity: O(|NUM_BUILDINGS| * i * j)
        self.code = lambda x: x[0] * len(grid[0]) + x[1]
        self.num_locations = 0
        self.num_buildings = 0
        self.visitable_by = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.num_locations += 1
                elif grid[i][j] == 1:
                    self.num_buildings += 1

                grid[i][j] = -grid[i][j]


        if self.num_locations == 0:
            return -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    self.bfs(grid, i, j)

        # print(grid)
        ret = 100000
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 0 and self.visitable_by[i][j] == self.num_buildings:
                    ret = min(grid[i][j], ret)

        if ret == 100000:
            return -1
        return ret


    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        queue = deque()
        queue.append((i, j, 0))
        visited = set()
        visited.add(self.code((i, j)))

        while len(queue) > 0:
            r, c, level = queue.popleft()
            new_level = level + 1

            if r > 0 and grid[r - 1][c] >= 0:
                code = self.code((r - 1, c))
                if code not in visited:
                    grid[r - 1][c] = grid[r - 1][c] + new_level
                    queue.append((r - 1, c, new_level))
                    visited.add(code)
                    self.visitable_by[r - 1][c] += 1


            if r < len(grid) - 1 and grid[r + 1][c] >= 0:
                code = self.code((r + 1, c))
                if code not in visited:
                    grid[r + 1][c] = grid[r + 1][c] + new_level
                    queue.append((r + 1, c, new_level))
                    visited.add(code)
                    self.visitable_by[r + 1][c] += 1


            if c > 0 and grid[r][c - 1] >= 0:
                code = self.code((r, c - 1))
                if code not in visited:
                    grid[r][c - 1] = grid[r][c - 1] + new_level
                    queue.append((r, c - 1, new_level))
                    visited.add(code)
                    self.visitable_by[r][c - 1] += 1

            if c < len(grid[0]) - 1 and grid[r][c + 1] >= 0:
                code = self.code((r, c + 1))
                if code not in visited:
                    grid[r][c + 1] = grid[r][c + 1] + new_level
                    queue.append((r, c + 1, new_level))
                    visited.add(code)
                    self.visitable_by[r][c + 1] += 1

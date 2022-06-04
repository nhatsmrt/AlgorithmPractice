class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Time and Space Complexity: O(mnk)

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        visited = set()
        MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        traverse = deque()

        init = (0, 0, 0) # top left, no obstacle removed
        visited.add(init)
        traverse.append((0, init))

        def is_valid_pos(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        while traverse:
            dist, (row, col, obs) = traverse.popleft()

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return dist

            for d_row, d_col in MOVES:
                n_row, n_col = row + d_row, col + d_col

                if is_valid_pos(n_row, n_col):
                    if grid[n_row][n_col] == 0: # no obstacle
                        n_obs = obs
                    else: # with obstacle
                        n_obs = obs + 1

                    n_state = (n_row, n_col, n_obs)
                    if n_obs <= k and n_state not in visited:
                        visited.add(n_state)
                        traverse.append((dist + 1, n_state))

        return -1

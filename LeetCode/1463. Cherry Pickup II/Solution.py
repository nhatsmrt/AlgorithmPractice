class Solution:
    COL_MOVES = [-1, 0, 1]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp = {}
        return self.pick(grid, 0, 0, len(grid[0]) - 1)

    def pick(self, grid: List[List[int]], row1, col1, col2) -> int:
        if (row1, col1, col2) in self.dp:
            return self.dp[(row1, col1, col2)]

        row2 = row1
        ret = grid[row1][col1]

        if (row1, col1) != (row2, col2):
            ret += grid[row2][col2]

        if row1 < len(grid) - 1:
            candidate_states = []
            next_moves = product(self.COL_MOVES, self.COL_MOVES)
            next_states = map(lambda mov: (row1 + 1, col1 + mov[0], col2 + mov[1]), next_moves)

            def is_legal(coords):
                return coords[0] >= 0 and coords[0] < len(grid) and coords[1] >= 0 and coords[1] < len(grid[0]) and coords[2] >= 0 and coords[2] < len(grid[0])

            legal_next_states = filter(is_legal, next_states)
            pick_fn = partial(self.pick, grid)

            ret += max(starmap(pick_fn, legal_next_states))


        self.dp[(row1, col1, col2)] = ret
        return ret

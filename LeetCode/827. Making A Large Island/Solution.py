class Solution:
    _MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)
        self.sizes = {}
        self.roots = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and ((i, j) not in self.roots):
                    self.compute_size(grid, (i, j), (i, j))

        ret = max([0] + [self.sizes[root] for root in self.sizes])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    ret = max(ret, self.change(grid, i, j))


        return ret

    def change(self, grid: List[int], i: int, j: int) -> int:
        ret = 1
        considered_roots = set()

        for move in self._MOVES:
            new_i, new_j = i + move[0], j + move[1]

            if self.is_valid(grid, (new_i, new_j)) and grid[new_i][new_j]:
                if (new_i, new_j) in self.sizes:
                    root = new_i, new_j
                else:
                    root = self.roots[(new_i, new_j)]

                if root not in considered_roots:
                    considered_roots.add(root)
                    ret += self.sizes[root]

        return ret


    def compute_size(self, grid: List[List[int]], cur_pos, root) -> int:
        if cur_pos != root:
            self.roots[cur_pos] = root

        ret = 1
        for move in self._MOVES:
            new_pos = cur_pos[0] + move[0], cur_pos[1] + move[1]

            if new_pos != root and new_pos not in self.sizes and new_pos not in self.roots and self.is_valid(grid, new_pos) and grid[new_pos[0]][new_pos[1]]:
                ret += self.compute_size(grid, new_pos, root)

        if cur_pos == root:
            self.sizes[root] = ret

        return ret

    def is_valid(self, grid, pos):
        return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])

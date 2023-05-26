def is_valid(pos, grid):
    row, col = pos
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 'W'


def count_killable(pos, dir, grid, solutions):
    key = (pos, dir)
    if key in solutions:
        return solutions[key]

    new_pos = pos[0] + dir[0], pos[1] + dir[1]
    if not is_valid(new_pos, grid):
        ret = 0
    else:
        ret = count_killable(new_pos, dir, grid, solutions)

        if grid[new_pos[0]][new_pos[1]] == 'E':
            ret += 1

    solutions[key] = ret
    return ret


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        solutions = {}
        ret = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    pos = row, col
                    cand = 0

                    for dir in DIRECTIONS:
                        cand += count_killable(pos, dir, grid, solutions)

                    ret = max(ret, cand)

        return ret

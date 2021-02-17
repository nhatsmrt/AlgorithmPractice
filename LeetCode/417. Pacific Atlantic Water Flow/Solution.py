class Solution:
    MOVES = [
        (-1, 0), (1, 0), (0, 1), (0, -1)
    ]

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time and Space Complexity: O(MN)

        if not matrix:
            return []

        pacific_water = set()
        atlantic_water = set()

        initial_pacific = [(i, 0) for i in range(len(matrix))] + [(0, j) for j in range(len(matrix[0]))]
        initial_atlantic = [(i, len(matrix[0]) - 1) for i in range(len(matrix))] + [(len(matrix) - 1, j) for j in range(len(matrix[0]))]

        self.flow(matrix, atlantic_water, set(initial_atlantic), initial_atlantic)
        self.flow(matrix, pacific_water, set(initial_pacific), initial_pacific)
        return pacific_water & atlantic_water


    def is_valid(self, pos, new_pos, matrix):
        return new_pos[0] >= 0 and new_pos[0] < len(matrix) and new_pos[1] >= 0 and new_pos[1] < len(matrix[0]) and matrix[pos[0]][pos[1]] <= matrix[new_pos[0]][new_pos[1]]


    def flow(self, matrix, ret: set, visited: set, to_traverse: list):
        while to_traverse:
            pos = to_traverse.pop()
            ret.add(pos)

            for move in self.MOVES:
                new_pos = pos[0] + move[0], pos[1] + move[1]
                if new_pos not in visited and self.is_valid(pos, new_pos, matrix):
                    to_traverse.append(new_pos)
                    visited.add(new_pos)

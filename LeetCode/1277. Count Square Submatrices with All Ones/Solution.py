class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        self.max_side = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret += self.find_max_side(matrix, i, j)


        return ret


    def find_max_side(self, matrix: List[List[int]], i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0 if matrix[i][j] == 0 else 1

        if self.max_side[i][j] != -1:
            return self.max_side[i][j]

        if matrix[i][j] == 0:
            return 0

        ret = 1 + min(
            self.find_max_side(matrix, i - 1, j),
            self.find_max_side(matrix, i, j - 1),
            self.find_max_side(matrix, i - 1, j - 1)
        )

        self.max_side[i][j] = ret
        return ret

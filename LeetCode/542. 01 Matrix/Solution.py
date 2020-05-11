class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 2D L1 distance transform
        # Time and Space Complexity: O(MN)

        ret = [
            [0 if matrix[i][j] == 0 else 1000000 for j in range(len(matrix[0]))]
            for i in range(len(matrix))
        ]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    ret[i][j] = min(ret[i][j], 1 + ret[i - 1][j])

                if j > 0:
                    ret[i][j] = min(ret[i][j], 1 + ret[i][j - 1])


        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if i + 1 < len(matrix):
                    ret[i][j] = min(ret[i][j], 1 + ret[i + 1][j])

                if j + 1 < len(matrix[0]):
                    ret[i][j] = min(ret[i][j], 1 + ret[i][j + 1])


        return ret

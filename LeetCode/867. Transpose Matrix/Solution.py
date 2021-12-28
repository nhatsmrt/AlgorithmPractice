class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time and Space Complexity: O(MN)
        ret = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret[j][i] = matrix[i][j]

        return ret

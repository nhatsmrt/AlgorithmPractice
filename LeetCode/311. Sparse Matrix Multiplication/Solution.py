class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        dok_A = self.build_dok(A)
        dok_B = self.build_dok(B, True)

        ret = [[0 for j in range(len(B[0]))] for i in range(len(A))]

        for i in dok_A:
            for k in dok_B:
                for j in dok_A[i]:
                    if j in dok_B[k]:
                        ret[i][k] += dok_A[i][j] * dok_B[k][j]

        return ret


    def build_dok(self, matrix: List[List[int]], reverse=False):
        dok = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    if reverse:
                        if j not in dok:
                            dok[j] = {}

                        dok[j][i] = matrix[i][j]

                    else:
                        if i not in dok:
                            dok[i] = {}

                        dok[i][j] = matrix[i][j]

        return dok

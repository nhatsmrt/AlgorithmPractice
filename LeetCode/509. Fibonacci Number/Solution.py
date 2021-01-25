class Solution:
    def fib(self, n: int) -> int:
        # Time and Space Complexity: O(log n)

        # X(n) = [F(n); F(n + 1)]
        # X(0) = [0; 1]
        # X(n) = [0 1; 1 1] X(n - 1) = [0 1; 1 1]^n - 0
        matrix = [[0, 1], [1, 1]]
        initial = [0, 1]

        return self.matrix_vect_mult(self.matrix_pow(matrix, n), initial)[0]


    def matrix_pow(self, mat: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1, 0], [0, 1]]

        if n:
            cur_pow_mat = mat

            while n > 0:
                if n & 1:
                    ret = self.matrix_matrix_mult(ret, cur_pow_mat)

                cur_pow_mat = self.matrix_matrix_mult(cur_pow_mat, cur_pow_mat)
                n //= 2

        return ret

    def matrix_matrix_mult(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ret = []

        for i in range(len(mat1)):
            ret.append([])
            for j in range(len(mat2[0])):
                ret[-1].append(sum([mat1[i][k] * mat2[k][j] for k in range(len(mat1[0]))]))

        return ret

    def matrix_vect_mult(self, mat: List[List[int]], vec: List[int]) -> List[int]:
        return [mat[i][0] * vec[0] + mat[i][1] * vec[1] for i in range(2)] 

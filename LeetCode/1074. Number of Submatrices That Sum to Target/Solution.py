class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(N^2)

        prefixes_r = []
        for i in range(len(matrix)):
            prefixes_r.append([0])

            for j in range(len(matrix[0])):
                prefixes_r[-1].append(prefixes_r[-1][-1] + matrix[i][j])


        ret = 0
        for c1 in range(len(matrix[0])):
            for c2 in range(c1, len(matrix[0])):
                aux = []
                for i in range(len(matrix)):
                    aux.append(prefixes_r[i][c2 + 1] - prefixes_r[i][c1])

                ret += self.numSumTarget(aux, target)

        return ret

    def numSumTarget(self, aux: List[int], target: int) -> int:
        prefix_inv_ind = {0: 1}

        cumsum = 0
        ret = 0
        for i in range(len(aux)):
            cumsum += aux[i]
            ret += prefix_inv_ind.get(cumsum - target, 0)
            prefix_inv_ind[cumsum] = prefix_inv_ind.get(cumsum, 0) + 1

        return ret

                

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Time Complexity: O(MN)
        # Space Complexity: O(MN); O(1) extra space
        if not (r * c == len(mat) * len(mat[0])):
            return mat


        ret = [[0 for j in range(c)] for i in range(r)]

        for ind in range(len(mat) * len(mat[0])):
            old_r = ind // len(mat[0])
            old_c = ind - old_r * len(mat[0])

            new_r = ind // c
            new_c = ind - new_r * c

            ret[new_r][new_c] = mat[old_r][old_c]

        return ret

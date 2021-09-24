class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Time and Space Complexity: O(MN)
        ret = []

        for row_ind, rs in enumerate(rowSum):
            col_ind = 0
            row = [0] * len(colSum)

            while rs > 0:
                row[col_ind] = min(colSum[col_ind], rs)
                rs -= row[col_ind]
                colSum[col_ind] -= row[col_ind]
                col_ind += 1

            ret.append(row)


        return ret

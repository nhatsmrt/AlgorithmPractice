class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # On each line parallel to the anti-diagonal, sum of coordinates is a constant

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        ret = []
        l = len(matrix) + len(matrix[0])

        for sum_coord in range(l - 1):
            # do stuff
            if sum_coord % 2 == 0:
                # going up
                r = min(len(matrix) - 1, sum_coord)
                c = sum_coord - r

                while r >= 0 and c < len(matrix[0]):
                    ret.append(matrix[r][c])
                    r -= 1
                    c += 1
            else:
                c = min(len(matrix[0]) - 1, sum_coord)
                r = sum_coord - c

                while r < len(matrix) and c >= 0:
                    ret.append(matrix[r][c])
                    r += 1
                    c -= 1

        return ret
        

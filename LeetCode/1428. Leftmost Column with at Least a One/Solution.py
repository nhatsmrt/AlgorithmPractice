# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n_row, n_col = binaryMatrix.dimensions()
        pointer = (n_row - 1, n_col - 1)
        ret = -1
        cur_best = -1

        while pointer[0] >= 0 and pointer[1] >= 0:
            if binaryMatrix.get(pointer[0], pointer[1]) == 0:
                if cur_best != -1 and (ret == -1 or cur_best < ret):
                    ret = cur_best
                pointer = (pointer[0] - 1, pointer[1])
            else:
                cur_best = pointer[1]
                pointer = (pointer[0], pointer[1] - 1)

        if cur_best != -1 and (ret == -1 or cur_best < ret):
            ret = cur_best

        return ret

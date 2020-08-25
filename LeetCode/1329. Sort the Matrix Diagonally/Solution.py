class Diagonal:
    def __init__(self, mat: List[List[int]], diff: int):
        self.mat = mat
        self.diff = diff

    def __len__(self):
        if self.diff >= 0:
            # lower left corner
            return len(self.mat) - self.diff
        else:
            # upper right corner
            return len(self.mat[0]) + self.diff

    def __getitem__(self, i: int):
        if self.diff >= 0:
            x, y = i + self.diff, i
        else:
            x, y = i, i - self.diff

        return (self.mat[x][y], x, y)

    def sort(self):
        data_and_inds = list(iter(self))
        inds = list(map(lambda tup: (tup[1], tup[2]), data_and_inds))
        data = sorted(map(lambda tup: tup[0], data_and_inds))

        for val, ind in zip(data, inds):
            self.mat[ind[0]][ind[1]] = val


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diffs = range(-len(mat[0]) + 1, len(mat))
        diagonals = map(lambda diff: Diagonal(mat, diff), diffs)

        for diagonal in diagonals:
            diagonal.sort()

        return mat
        

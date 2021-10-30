class UnionFind:
    def __init__(self):
        self.par, self.weight = {}, {}

    def union(self, pos1, pos2):
        root1, root2 = self.find(pos1), self.find(pos2)

        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.weight[root2] += self.weight[root1]
                self.par[root1] = root2
            else:
                self.weight[root1] += self.weight[root2]
                self.par[root2] = root1

    def find(self, pos):
        if pos not in self.par:
            self.par[pos] = pos
            self.weight[pos] = 1

        if self.par[pos] == pos:
            return pos

        ret = self.find(self.par[pos])
        self.par[pos] = ret
        return ret



class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # Time Complexity: O(MN alpha(MN))
        # Space Complexity: O(MN)

        values = set()
        index = {}

        for i, j in product(range(len(A)), range(len(A[0]))):
            values.add(A[i][j])

            if A[i][j] not in index:
                index[A[i][j]] = set()

            index[A[i][j]].add((i, j))

        uf = UnionFind()
        values = sorted(list(values), reverse=True)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(pos):
            return pos[0] >= 0 and pos[0] < len(A) and pos[1] >= 0 and pos[1] < len(A[0])

        for value in values:
            for pos in index[value]:
                for move in moves:
                    new_pos = pos[0] + move[0], pos[1] + move[1]

                    if is_valid(new_pos) and A[new_pos[0]][new_pos[1]] >= A[pos[0]][pos[1]]:
                        uf.union(pos, new_pos)

            if uf.find((0, 0)) == uf.find((len(A) - 1, len(A[0]) - 1)):
                return value

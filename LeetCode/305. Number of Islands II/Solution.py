class UnionFind:
    def __init__(self):
        self.par = {}
        self.weight = {}

    def add(self, pos):
        self.par[pos] = pos
        self.weight[pos] = 1

    def union(self, pos1, pos2):
        root1, root2 = self.find(pos1), self.find(pos2)

        if root1 == root2:
            return False

        # union-by-weight
        if self.weight[root1] < self.weight[root2]:
            self.par[root1] = root2
            self.weight[root2] += self.weight[root1]
        else:
            self.par[root2] = root1
            self.weight[root1] += self.weight[root2]
        return True

    def find(self, pos):
        if self.par[pos] == pos:
            return pos

        ret = self.find(self.par[pos])
        self.par[pos] = ret  # path compresssion
        return ret


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Time Complexity: O(k * alpha(k))
        # Space Complexity: O(k)

        uf = UnionFind()
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_cc = 0
        ret = []

        for pos in positions:
            pos = tuple(pos)

            if pos not in uf.par:  # deduplicate
                uf.add(pos)
                num_cc += 1

                for move in moves:
                    neigh = pos[0] + move[0], pos[1] + move[1]

                    if neigh[0] >= 0 and neigh[0] < m and neigh[1] >= 0 and neigh[1] < n and neigh in uf.par:
                        if uf.union(neigh, pos):
                            num_cc -= 1

                ret.append(num_cc)
            else:
                ret.append(ret[-1])

        return ret

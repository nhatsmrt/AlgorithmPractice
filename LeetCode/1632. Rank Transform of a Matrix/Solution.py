class UnionFind:
    def __init__(self):
        self.par = {}
        self.weight = {}
        self.from_list = {}
        self.to_list = {}
        self.rank = {}

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            weight1, weight2 = self.weight.get(root1, 1), self.weight.get(root2, 1)

            if weight1 <= weight2:
                self.par[root1] = root2
                self.weight[root2] += self.weight[root1]
            else:
                self.par[root2] = root1
                self.weight[root1] += self.weight[root2]


    def find(self, node):
        if self.par.get(node, node) == node:
            self.par[node] = node
            self.weight[node] = self.weight.get(node, 1)
            return node

        else:
            ret = self.find(self.par[node])
            self.par[node] = ret  # path compression
            return ret

    def add_edge(self, from_node, to_node):
        from_root, to_root = self.find(from_node), self.find(to_node)

        if from_root not in self.from_list:
            self.from_list[from_root] = set()

        if to_root not in self.to_list:
            self.to_list[to_root] = set()

        self.from_list[from_root].add(to_root)
        self.to_list[to_root].add(from_root)


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(MN log MN)
        # Space Complexity: O(MN)

        ret = [[1 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        uf = UnionFind()

        for i in range(len(matrix)):
            row_ind = {}

            for j in range(len(matrix[0])):
                if matrix[i][j] in row_ind:
                    uf.union((i, j), row_ind[matrix[i][j]])
                else:
                    row_ind[matrix[i][j]] = (i, j)

        for j in range(len(matrix[0])):
            col_ind = {}

            for i in range(len(matrix)):
                if matrix[i][j] in col_ind:
                    uf.union((i, j), col_ind[matrix[i][j]])
                else:
                    col_ind[matrix[i][j]] = (i, j)

        all_vals = [(matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]

        all_vals.sort()
        row_data = {}
        col_data = {}

        for val, i, j in all_vals:
            if i not in row_data:
                row_rank = 1
            elif matrix[row_data[i][0]][row_data[i][1]] != val:
                row_rank = uf.rank[uf.find(row_data[i])] + 1
            else:
                row_rank = uf.rank[uf.find(row_data[i])]

            if j not in col_data:
                col_rank = 1
            elif matrix[col_data[j][0]][col_data[j][1]] != val:
                col_rank = uf.rank[uf.find(col_data[j])] + 1
            else:
                col_rank = uf.rank[uf.find(col_data[j])]

            true_rank = max(row_rank, col_rank, uf.rank.get(uf.find((i, j)), 1))
            row_data[i] = (i, j)
            col_data[j] = (i, j)

            uf.rank[uf.find((i, j))] = true_rank

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret[i][j] = uf.rank[uf.find((i, j))]

        return ret

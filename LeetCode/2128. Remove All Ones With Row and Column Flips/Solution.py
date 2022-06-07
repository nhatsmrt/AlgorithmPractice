class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # Time and Space Complexity: O(MN)

        out_edges = {}
        in_edges = {}


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row = (i, True, True)
                neg_row = (i, True, False)
                col = (j, False, True)
                neg_col = (j, False, False)

                all_var = [row, neg_row, col, neg_col]

                for var in all_var:
                    if var not in out_edges:
                        out_edges[var] = set()
                        in_edges[var] = set()

                if grid[i][j]: # flip either row and col, but not both
                    out_edges[row].add(neg_col)
                    out_edges[neg_row].add(col)

                    out_edges[col].add(neg_row)
                    out_edges[neg_col].add(row)
                else: # flip both or neither
                    out_edges[row].add(col)
                    out_edges[col].add(row)

                    out_edges[neg_row].add(neg_col)
                    out_edges[neg_col].add(neg_row)


        # strongly-connected component (Kosaraju's algorithm)
        # first pass:
        visited = set()
        finished = []
        assigned = {node: None for node in out_edges}

        for node in out_edges:
            if node not in visited:
                self.first_pass(node, out_edges, visited, finished)

        # reverse the graph:

        for first in out_edges:
            for second in out_edges[first]:
                in_edges[second].add(first)

        for node in reversed(finished):
            if not assigned[node]:
                self.assign(node, node, in_edges, assigned)

        for i in range(len(grid)):
            row = (i, True, True)
            neg_row = (i, True, False)

            if assigned[row] == assigned[neg_row]:
                return False

        for j in range(len(grid[0])):
            col = (j, False, True)
            neg_col = (j, False, False)

            if assigned[col] == assigned[neg_col]:
                return False

        return True

    def first_pass(self, node, out_edges, visited, finished):
        visited.add(node)

        for neigh in out_edges[node]:
            if neigh not in visited:
                self.first_pass(neigh, out_edges, visited, finished)

        finished.append(node)

    def assign(self, node, root, in_edges, assigned):
        assigned[node] = root

        for neigh in in_edges[node]:
            if not assigned[neigh]:
                self.assign(neigh, root, in_edges, assigned)

class Solution:
    # In-Out DP
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # O(|V|) time and space complexity

        self.adjList = [[] for i in range(len(edges) + 1)]
        for edge in edges:
            self.adjList[edge[0]].append(edge[1])
            self.adjList[edge[1]].append(edge[0])

        self.in_dp = [None] * (len(edges) + 1)
        self.out = [None] * (len(edges) + 1)
        self.parent = [None] * (len(edges) + 1)
        self.children = [[] for i in range(len(edges) + 1)]
        self.best_child = [[] for i in range(len(edges) + 1)]

        # Build tree, rooted at 0
        self.parent[0] = -1
        self.build_tree(0)

        # Compute in[n], distance to the furthest node inside n's subtree
        # in[n] = 1 + max_c(in[c]), where c are in's children
        self.compute_in_diam(0)

        # Compute out[n], distance to the furthest node outside n's subtree
        # out[n] = max(1 + out[n.p], 2 + max_{sibling} (in[sibling]))
        self.compute_out_diam(0)

        # Compute the diameter
        ret = 0
        for i in range(len(self.in_dp)):
            ret = max(ret, self.in_dp[i], self.out[i])

        return ret

    def build_tree(self, node):
        for neighbor in self.adjList[node]:
            if self.parent[neighbor] == None:
                self.parent[neighbor] = node
                self.children[node].append(neighbor)
                self.build_tree(neighbor)

    def compute_in_diam(self, node: int):
        if self.in_dp[node] is not None:
            return self.in_dp[node]

        values = [self.compute_in_diam(child) for child in self.children[node]]
        if len(values) == 0:
            self.in_dp[node] = 0
            return 0
        elif len(values) == 1:
            self.in_dp[node] = 1 + values[0]
            self.best_child[node].append((self.children[node][0], values[0]))
        else:
            self.in_dp[node] = 1 + max(values)

            best = 0 if values[0] > values[1] else 1
            second_best = 1 - best

            for i in range(2, len(values)):
                if values[i] > values[best]:
                    second_best = best
                    best = i
                elif values[i] > values[second_best]:
                    second_best = i

            self.best_child[node].append((self.children[node][best], values[best]))
            self.best_child[node].append((self.children[node][second_best],
                                          values[second_best]))

        return self.in_dp[node]

    def compute_out_diam(self, node: int):
        if self.parent[node] == -1:
            self.out[node] = 0
        else:
            parent = self.parent[node]
            candidates = []
            candidates.append(self.out[parent] + 1)

            if len(self.best_child[parent]) > 1:
                if node == self.best_child[parent][0][0]:
                    candidates.append(self.best_child[parent][1][1] + 2)
                else:
                    candidates.append(self.best_child[parent][0][1] + 2)

            self.out[node] = max(candidates) if len(candidates) > 0 else 0
        for child in self.children[node]:
            self.compute_out_diam(child)


    

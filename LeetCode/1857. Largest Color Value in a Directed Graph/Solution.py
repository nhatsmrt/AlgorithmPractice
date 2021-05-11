class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Time and Space Complexity: O(min(|Sigma|, V) (V + E))

        self.dp = {}
        self.colors = colors
        self.adj_lists = {i: set() for i in range(len(colors))}

        for edge in edges:
            self.adj_lists[edge[0]].add(edge[1])

        ret = 0
        for node, color in enumerate(colors):
            cand = self.find_path_val(node, color, set())

            if cand == -1:
                return -1

            ret = max(cand, ret)

        return ret



    def find_path_val(self, node: int, color: str, ancestors: set) -> int:
        if (node, color) in self.dp:
            return self.dp[(node, color)]

        ancestors.add(node)
        ret = 0

        for child in self.adj_lists[node]:
            if child in ancestors:
                return -1

            cand = self.find_path_val(child, color, ancestors)
            if cand == -1:
                return -1

            ret = max(ret, cand)


        ancestors.remove(node)

        if self.colors[node] == color:
            ret += 1

        self.dp[(node, color)] = ret
        return ret

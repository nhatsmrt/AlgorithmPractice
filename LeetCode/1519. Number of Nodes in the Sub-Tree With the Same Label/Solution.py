class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Time Complexity: O(N log N)

        # The number of set insertion involving a node
        # is upper bounded by the number of ancestors of the node
        # that are not the heavy children of their parents
        # which is O(log N)

        ret = [1] * n
        children = {i: set() for i in range(n)}
        parent = {}
        adj_list = {i: set() for i in range(n)}

        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        # Build tree:
        self.build_tree(0, adj_list, children, parent)

        for i in range(n):
            if i not in parent:
                # i is root
                self.dfs(i, ret, children, labels)
        return ret

    def build_tree(self, node, adj_list, children, parent):
        for neighbor in adj_list[node]:
            if neighbor != parent.get(node):
                parent[neighbor] = node
                children[node].add(neighbor)
                self.build_tree(neighbor, adj_list, children, parent)

    def dfs(self, node: int, ret: List[int], children: dict, labels: str):
        if not children[node]:  # node is leaf:
            return Counter([labels[node]])

        children_cnt = {child: self.dfs(child, ret, children, labels) for child in children[node]}

        for child in children_cnt:
            ret[node] += children_cnt[child][labels[node]]


        # Small-to-large merging (i.e Sack/DSU on tree):
        max_child = max(children_cnt, key=lambda k: len(children_cnt[k]))
        for child in children_cnt:
            if child != max_child:
                for label in children_cnt[child]:
                    children_cnt[max_child][label] += children_cnt[child][label]

        children_cnt[max_child][labels[node]] += 1
        return children_cnt[max_child]

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # Time and Space Complexity: O(V + E)
        # Idea: sum(node's degree) = 2 |E| => must be even
        # => number of odd degree nodes must be even

        adj_lists = {i: set() for i in range(n)}

        for node1, node2 in edges:
            adj_lists[node1 - 1].add(node2 - 1)
            adj_lists[node2 - 1].add(node1 - 1)

        odd_nodes = []

        for node in range(n):
            if len(adj_lists[node]) % 2 == 1:
                odd_nodes.append(node)

        if not odd_nodes:
            return True

        if len(odd_nodes) > 4:
            return False

        if len(odd_nodes) == 4:
            # must connect to each other!
            node1, node2, node3, node4 = odd_nodes
            return \
            (node1 not in adj_lists[node2] and node3 not in adj_lists[node4]) or \
            (node1 not in adj_lists[node3] and node2 not in adj_lists[node4]) or \
            (node1 not in adj_lists[node4] and node2 not in adj_lists[node3])

        # 2 odd nodes!
        node1, node2 = odd_nodes[0], odd_nodes[1]

        # direct connect
        if node2 not in adj_lists[node1]:
            return True

        # connect to the same node
        for common in range(n):
            if common not in (node1, node2) and common not in adj_lists[node1] and common not in adj_lists[node2]:
                return True

        return False

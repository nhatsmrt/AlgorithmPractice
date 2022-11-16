class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # Idea: sum(road's importance) = sum(node's value * number of roads node is adjacent to)
        # By rearrangement inequality, this sum is maximized when
        # the nodes' assigned value is in the same sorted order
        # as the nodes' number of adjacent roads.

        adjacency_cnt = Counter()

        for n1, n2 in roads:
            adjacency_cnt[n1] += 1
            adjacency_cnt[n2] += 1

        ret = 0
        for i, node in enumerate(sorted(range(n), key=lambda n: adjacency_cnt[n])):
            ret += (i + 1) * adjacency_cnt[node]

        return ret

INF = 201


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_lists = {}

        for start, end in redEdges:
            start_node = (start, 1)
            end_node = (end, 0)

            if start_node not in adj_lists:
                adj_lists[start_node] = set()

            adj_lists[start_node].add(end_node)

        for start, end in blueEdges:
            start_node = (start, 0)
            end_node = (end, 1)

            if start_node not in adj_lists:
                adj_lists[start_node] = set()

            adj_lists[start_node].add(end_node)


        visited = set([(0, 0), (0, 1)])
        dists = [-1] * n
        dists[0] = 0
        traverse = deque([(0, 0, 0), (0, 1, 0)])

        while traverse:
            value, col, dist = traverse.popleft()
            dists[value] = dist if dists[value] == -1 else min(dists[value], dist)

            for next_value, next_col in adj_lists.get((value, col), []):
                if (next_value, next_col) not in visited:
                    visited.add((next_value, next_col))
                    traverse.append((next_value, next_col, dist + 1))

        return dists

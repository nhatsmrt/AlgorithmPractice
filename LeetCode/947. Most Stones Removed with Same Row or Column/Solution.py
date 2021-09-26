def dfs(stone, adj_lists, visited):
    visited.add(stone)

    for next_stone in adj_lists.get(stone, []):
        if next_stone not in visited:
            dfs(next_stone, adj_lists, visited)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Time and Space Complexity: O(V + E)

        adj_lists = {}
        rows = {}
        cols = {}

        stones = list(map(tuple, stones))

        for stone in stones:
            if stone[0] not in rows:
                rows[stone[0]] = set()

            rows[stone[0]].add(stone)

            if stone[1] not in cols:
                cols[stone[1]] = set()

            cols[stone[1]].add(stone)

        for index in [rows, cols]:
            for ind in index:
                for pos1 in index[ind]:
                    for pos2 in index[ind]:
                        if pos1 != pos2:
                            if pos1 not in adj_lists:
                                adj_lists[pos1] = set()

                            if pos2 not in adj_lists:
                                adj_lists[pos2] = set()

                            adj_lists[pos1].add(pos2)
                            adj_lists[pos2].add(pos1)

        num_components = 0
        visited = set()

        for stone in stones:
            if stone not in visited:
                num_components += 1
                dfs(stone, adj_lists, visited)

        return len(stones) - num_components

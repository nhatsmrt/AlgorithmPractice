class Solution:
    MOVES = [(1, 0), (0, 1)]

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN log W)

        low = 0
        high = max(heights[i][j] for i in range(len(heights)) for j in range(len(heights[i])))


        while low < high:
            candidate = low + (high - low) // 2

            if self.is_reachable(candidate, heights):
                high = candidate
            else:
                low = candidate + 1

        return low

    def is_reachable(self, limit, heights):
        adj_lists = {(i, j): set() for j in range(len(heights[0])) for i in range(len(heights))}

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                for move in self.MOVES:
                    new_i, new_j = i + move[0], j + move[1]

                    if self.is_valid((i, j), (new_i, new_j), limit, heights):
                        adj_lists[(i, j)].add((new_i, new_j))
                        adj_lists[(new_i, new_j)].add((i, j))
        return self.dfs((0, 0), (len(heights) - 1, len(heights[0]) - 1), adj_lists, set())

    def dfs(self, cur, target, adj_lists, visited):
        if cur == target:
            return True

        visited.add(cur)
        for neighbor in adj_lists[cur]:
            if neighbor not in visited and self.dfs(neighbor, target, adj_lists, visited):
                return True

        return False


    def is_valid(self, cur_pos, next_pos, limit, heights):
        return next_pos[0] >= 0 and next_pos[0] < len(heights) and next_pos[1] >= 0 and next_pos[1] < len(heights[0]) and abs(heights[cur_pos[0]][cur_pos[1]] - heights[next_pos[0]][next_pos[1]]) <= limit

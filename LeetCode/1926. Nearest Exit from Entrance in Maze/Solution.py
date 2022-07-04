class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Time and Space Complexity: O(MN)

        init = tuple(entrance)

        traverse = deque()
        traverse.append((0, init))

        visited = {init}

        def is_valid(row, col):
            return row >= 0 and row < len(maze) and col >= 0 and col < len(maze[0]) and maze[row][col] == '.'

        def is_entrance(row, col):
            return row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1 and maze[row][col] == '.'

        MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while traverse:
            dist, (row, col) = traverse.popleft()

            if is_entrance(row, col) and (row, col) != init:
                return dist

            for dr, dc in MOVES:
                new_r, new_c = row + dr, col + dc

                if is_valid(new_r, new_c) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    traverse.append((dist + 1, (new_r, new_c)))

        return -1

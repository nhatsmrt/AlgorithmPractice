class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Time and Space Complexity: O(MN)

        INF = 2147483647
        queues = deque()

        for i, j in product(range(len(rooms)), range(len(rooms[0]))):
            if rooms[i][j] == 0:
                queues.append((i, j, 0))

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(i, j):
            return i >= 0 and i < len(rooms) and j >= 0 and j < len(rooms[0])

        while queues:
            i, j, dist = queues.popleft()

            for move in moves:
                new_i, new_j = i + move[0], j + move[1]

                if is_valid(new_i, new_j) and rooms[new_i][new_j] == INF: # unvisited
                    rooms[new_i][new_j] = dist + 1
                    queues.append((new_i, new_j, dist + 1))

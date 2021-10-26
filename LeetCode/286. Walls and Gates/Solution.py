class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Time and Space Complexity: O(MN)

        INF = 2147483647
        levels = {}

        for i, j in product(range(len(rooms)), range(len(rooms[0]))):
            if rooms[i][j] == 0:
                levels[len(levels)] = [(i, j)], 0

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(i, j):
            return i >= 0 and i < len(rooms) and j >= 0 and j < len(rooms[0])

        while levels:
            new_levels = {}

            for levels_ind in levels:
                level, dist = levels[levels_ind]
                new_level = []

                for i, j in level:
                    for move in moves:
                        new_i, new_j = i + move[0], j + move[1]

                        if is_valid(new_i, new_j) and rooms[new_i][new_j] == INF: # unvisited
                            rooms[new_i][new_j] = dist + 1
                            new_level.append((new_i, new_j))

                if new_level:
                    new_levels[levels_ind] = new_level, dist + 1

            levels = new_levels                    

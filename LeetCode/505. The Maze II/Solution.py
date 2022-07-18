class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Time and Space Complexity: O(MN)

        start = tuple(start)
        destination = tuple(destination)

        def is_valid(pos):
            return pos[0] >= 0 and pos[0] < len(maze) and pos[1] >= 0 and pos[1] < len(maze[0]) and maze[pos[0]][pos[1]] == 0

        def move(pos, direction):
            return pos[0] + direction[0], pos[1] + direction[1]

        to_traverse = deque()
        visited = set()

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        for direction in directions:
            state = start, direction

            to_traverse.append((0, state))
            visited.add(state)

        while to_traverse:
            dist, (pos, direction) = to_traverse.popleft()
            new_position = move(pos, direction)
            new_state = new_position, direction

            if pos == destination and not is_valid(new_position):
                return dist

            if is_valid(new_position):
                if new_state not in visited:
                    to_traverse.append((dist + 1, new_state))
                    visited.add(new_state)
            else: # stops
                for new_direction in directions:
                    new_position = move(pos, new_direction)
                    new_state = new_position, new_direction

                    if is_valid(new_position) and new_state not in visited:
                        to_traverse.append((dist + 1, new_state))
                        visited.add(new_state)

        return -1

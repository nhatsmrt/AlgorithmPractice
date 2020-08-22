from typing import Tuple


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        return self.dfs(maze, set(), (start[0], start[1]), (destination[0], destination[1]))

    def dfs(self, maze, visited: set, pos: Tuple[int, int], destination: Tuple[int, int]) -> bool:
        if pos not in visited:
            if pos == destination:
                return True

            visited.add(pos)

            # roll up:
            new_pos = [pos[0], pos[1]]
            while new_pos[0] > 0 and maze[new_pos[0] - 1][pos[1]] == 0:
                new_pos[0] -= 1
            new_pos = tuple(new_pos)

            if self.dfs(maze, visited, new_pos, destination):
                return True

            # roll down:
            new_pos = [pos[0], pos[1]]
            while new_pos[0] < len(maze) - 1 and maze[new_pos[0] + 1][pos[1]] == 0:
                new_pos[0] += 1
            new_pos = tuple(new_pos)


            if self.dfs(maze, visited, new_pos, destination):
                return True

            # roll left:
            new_pos = [pos[0], pos[1]]
            while new_pos[1] > 0 and maze[pos[0]][new_pos[1] - 1] == 0:
                new_pos[1] -= 1
            new_pos = tuple(new_pos)


            if self.dfs(maze, visited, new_pos, destination):
                return True

            # roll right:
            new_pos = [pos[0], pos[1]]
            while new_pos[1] < len(maze[0]) - 1 and maze[pos[0]][new_pos[1] + 1] == 0:
                new_pos[1] += 1
            new_pos = tuple(new_pos)


            if self.dfs(maze, visited, new_pos, destination):
                return True

        return False

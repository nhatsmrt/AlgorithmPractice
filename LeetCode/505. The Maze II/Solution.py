from typing import Tuple

def compute_dist(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        start = start[0], start[1]
        dest = destination[0], destination[1]

        visited = {start: 0}
        to_visit = [(0, start)]

        while to_visit:
            dist, pos = 10000000, (-1, -1)

            for cand_dist, cand_pos in to_visit:
                if cand_dist < dist:
                    dist = cand_dist
                    pos = cand_pos

            to_visit.remove((dist, pos))

            if pos == dest:
                return dist

            # roll up:
            x, y = pos[0], pos[1]
            while x - 1 >= 0 and maze[x - 1][y] == 0:
                x -= 1

            new_dist = dist + compute_dist(pos, (x, y))
            if (x, y) not in visited:
                visited[(x, y)] = new_dist
                to_visit.append((new_dist, (x, y)))
            elif visited[(x, y)] > new_dist:
                visited[(x, y)] = new_dist
                for i in range(len(to_visit)):
                    cand_dist, cand_pos = to_visit[i]

                    if cand_pos == (x, y):
                        to_visit[i] = (new_dist, (x, y))
                        break


            # roll down:
            x, y = pos[0], pos[1]
            while x + 1 < len(maze) and maze[x + 1][y] == 0:
                x += 1

            new_dist = dist + compute_dist(pos, (x, y))
            if (x, y) not in visited:
                visited[(x, y)] = new_dist
                to_visit.append((new_dist, (x, y)))
            elif visited[(x, y)] > new_dist:
                visited[(x, y)] = new_dist
                for i in range(len(to_visit)):
                    cand_dist, cand_pos = to_visit[i]

                    if cand_pos == (x, y):
                        to_visit[i] = (new_dist, (x, y))

            # roll left:
            x, y = pos[0], pos[1]
            while y - 1 >= 0 and maze[x][y - 1] == 0:
                y -= 1

            new_dist = dist + compute_dist(pos, (x, y))
            if (x, y) not in visited:
                visited[(x, y)] = new_dist
                to_visit.append((new_dist, (x, y)))
            elif visited[(x, y)] > new_dist:
                visited[(x, y)] = new_dist
                for i in range(len(to_visit)):
                    cand_dist, cand_pos = to_visit[i]

                    if cand_pos == (x, y):
                        to_visit[i] = (new_dist, (x, y))

            # roll right:
            x, y = pos[0], pos[1]
            while y + 1 < len(maze[0]) and maze[x][y + 1] == 0:
                y += 1

            new_dist = dist + compute_dist(pos, (x, y))
            if (x, y) not in visited:
                visited[(x, y)] = new_dist
                to_visit.append((new_dist, (x, y)))
            elif visited[(x, y)] > new_dist:
                visited[(x, y)] = new_dist
                for i in range(len(to_visit)):
                    cand_dist, cand_pos = to_visit[i]

                    if cand_pos == (x, y):
                        to_visit[i] = (new_dist, (x, y))

        return -1

from functools import partial
from itertools import starmap
from typing import Tuple


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # Time and Space Complexity: O(MN)

        self.moves = [
            (0, 1), (1, 0), (0, -1), (-1, 0)
        ]


        island_1 = set()
        island_2 = set()

        for i in range(len(A)):
            for j in range(len(A[0])):
                self.determine_island(A, i, j, island_1, island_2)

        to_visit = collections.deque()
        for pos in island_1:
            to_visit.append((pos, 0))

        visited = copy.deepcopy(island_1)
        dist = 0

        while to_visit:
            pos, dist = to_visit.popleft()

            if pos in island_2:
                return dist - 1

            neighbors = self.move(A, pos[0], pos[1])

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    to_visit.append((neighbor, dist + 1))

    def determine_island(self, A, i, j, island_1, island_2):
        if A[i][j] == 1:
            # is land
            neighbors = self.move(A, i, j)

            for neighbor in neighbors:
                if abs(A[neighbor[0]][neighbor[1]]) == 1:
                    if neighbor in island_1:
                        island_1.add((i, j))
                        break
                    elif neighbor in island_2:
                        island_2.add((i, j))
                        break
            else:
                if island_1:
                    island_2.add((i, j))
                else:
                    island_1.add((i, j))

            A[i][j] = -1
            floodfill_fn = partial(self.determine_island, A, island_1=island_1, island_2=island_2)

            list(starmap(floodfill_fn, neighbors))

    def move(self, A, i: int, j: int) -> List[Tuple[int, int]]:
        def move_fn(move):
            return move[0] + i, move[1] + j

        return list(filter(partial(self.is_valid, A), map(move_fn, self.moves)))

    def is_valid(self, A: List[List[int]], coords: Tuple[int, int]) -> bool:
        i, j = coords
        return i >= 0 and i < len(A) and j >= 0 and j < len(A[0])

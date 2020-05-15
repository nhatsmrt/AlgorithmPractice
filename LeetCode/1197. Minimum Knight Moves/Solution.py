from typing import Tuple

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


class PriorityQueue:
    def __init__(self, data):
        self.data = data
        heapq.heapify(self.data)
        self.index = {}

        for i in range(len(data)):
            self.index[self.data[i][1]] = i

    def offer(self, priority: int, point: Tuple[int, int]):
        if len(self.data) == 0:
            self.data = [(priority, point)]
            self.index[point] = 0
        else:
            self.data.append([priority, point])
            self.index[point] = len(self.data) - 1
            self.sift_up(len(self.data) - 1)

    def poll(self) -> Tuple[int, int, int]:
        if len(self.data) == 1:
            ret = self.data[0]

            self.data = []
            self.index = {}

            return ret

        ret = self.data[0]
        self.data[0] = self.data.pop()
        self.index.pop(ret[1])
        self.index[self.data[0][1]] = 0
        self.sift_down(0)

        return ret

    def decrease_priority(self, point: int, new_priority: int):
        i = self.index[point]
        self.data[i][0] = new_priority
        self.sift_up(i)

    def sift_up(self, i: int):
        if i != i // 2 and self.data[i // 2][0] > self.data[i][0]:
            self.swap(i, i // 2)
            self.sift_up(i // 2)

    def sift_down(self, i: int):
        if i * 2 + 1 < len(self.data):
            child = 2 * i + 1

            if i * 2 + 2 < len(self.data) and self.data[i * 2 + 2][0] < self.data[i * 2 + 1][0]:
                child = 2 * i + 2

            if self.data[i][0] > self.data[child][0]:
                self.swap(i, child)
                self.sift_down(child)

    def swap(self, i: int, j: int):
        self.index[self.data[i][1]] = j
        self.index[self.data[j][1]] = i

        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # A* search

        self.target = (x, y)
        pq = PriorityQueue([[0, (0, 0)]])
        dist = {(0, 0): 0}


        while True:
            priority, point = pq.poll()

            if point == (x, y):
                return round(priority + self.potential((0, 0)))

            neighbors = self.generate_neighbors(point)

            for neighbor in neighbors:
                neighbor_priority = \
                priority + 1 + self.potential(neighbor) - self.potential(point)

                if neighbor not in dist or dist[neighbor] > neighbor_priority:
                    dist[neighbor] = neighbor_priority

                    if neighbor in pq.index:
                        pq.decrease_priority(neighbor, neighbor_priority)
                    else:
                        pq.offer(neighbor_priority, neighbor)

    def generate_neighbors(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        ret = []

        for move in moves:
            ret.append((start[0] + move[0], start[1] + move[1]))

        return ret


    def manhattan(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def euclidean(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def potential(self, point):
        # return self.manhattan(point, self.target) / 3
        return self.euclidean(point, self.target) / math.sqrt(5)

class Event:
    def __init__(self, pos, height, ind, left):
        self.pos, self.height, self.ind, self.left = pos, height, ind, left

    def __repr__(self):
        return str(self.pos) + "_" + str(height) + "_" + str(self.ind) + "_" + str(self.left)


class MultisetHeapBST:
    def __init__(self):
        self.multiset = dict()
        self.heap = []

    def add(self, val):
        if val not in self.multiset:
            heapq.heappush(self.heap, val)
            self.multiset[val] = 1
        else:
            self.multiset[val] += 1

    def remove(self, val):
        if val not in self.multiset:
            raise ValueError()
        else:
            self.multiset[val] -= 1
            if self.multiset[val] == 0:
                del self.multiset[val]

    def get_min(self):
        while self.heap[0] not in self.multiset:
            heapq.heappop(self.heap)
        return self.heap[0]

    def __len__(self):
        return len(self.multiset)


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        vertical_events = []
        for i in range(len(buildings)):
            vertical_events.append(Event(buildings[i][0], buildings[i][-1], i, True))
            vertical_events.append(Event(buildings[i][1], buildings[i][-1], i, False))

        vertical_events.sort(key=lambda ev: ev.pos)
        start = end = cur_x = vertical_events[0].pos
        i = 1
        cur_height = vertical_events[0].height

        consider_heights = MultisetHeapBST()
        consider_heights.add(-vertical_events[0].height)
        keypoints = []

        for i in range(1, len(vertical_events)):

            if vertical_events[i].left:
                consider_heights.add(-vertical_events[i].height)
            else:
                consider_heights.remove(-vertical_events[i].height)

            if vertical_events[i].height >= cur_height:
                end = vertical_events[i].pos

            if vertical_events[i].pos == start:
                if vertical_events[i].height > cur_height:
                    cur_height = vertical_events[i].height
            else:
                if len(consider_heights) > 0:
                    max_height = -consider_heights.get_min()
                    if max_height != cur_height:
                        keypoints.append([start, cur_height])
                        cur_height = max_height
                        start = end
                else:
                    if (
                        i == len(vertical_events) - 1
                        or vertical_events[i + 1].pos > vertical_events[i].pos
                       ):
                        keypoints.append([start, cur_height])

                    if i < len(vertical_events) - 1:
                        if vertical_events[i + 1].pos > vertical_events[i].pos:
                            cur_height = 0
                            start = vertical_events[i].pos

        keypoints.append([vertical_events[-1].pos, 0])
        return keypoints

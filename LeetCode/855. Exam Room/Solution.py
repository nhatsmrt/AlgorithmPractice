from sortedcontainers import SortedList


class ExamRoom:

    def __init__(self, n: int):
        # Time Complexity (initialization): O(1)
        # Space Complexity (overall): O(N)

        # intervals: (width, neg_placement, start, end)
        # start: start_ind -> (width, placement, start, end)
        # end: end_ind -> (width, placement, start, end)

        self.n = n
        self.intervals = SortedList()
        self.starts = {}
        self.ends = {}

        self.insert(0, n - 1)

    def get_width_placement(self, start, end):
        # Time Complexity: O(log N)
        if start == 0:
            return (end, 0)
        elif end == self.n - 1:
            return (self.n - 1 - start, self.n - 1)
        else:
            return ((end - start) // 2, (start + end) // 2)

    def seat(self) -> int:
        # Time Complexity: O(log N)
        width, neg_placement, start, end = self.intervals.pop()
        placement = -neg_placement
        self.starts.pop(start)
        self.ends.pop(end)


        if placement - 1 >= start:
            self.insert(start, placement - 1)

        if placement + 1 <= end:
            self.insert(placement + 1, end)

        return placement

    def insert(self, start, end):
        width, placement = self.get_width_placement(start, end)
        self.intervals.add((width, -placement, start, end))
        self.starts[start] = (width, -placement, start, end)
        self.ends[end] = (width, -placement, start, end)


    def leave(self, p: int) -> None:
        start, end = p, p

        if p - 1 in self.ends:
            _, _, start, _ = self.ends[p - 1]
            self.intervals.remove(self.ends[p - 1])
            self.ends.pop(p - 1)

        if p + 1 in self.starts:
            _, _, _, end = self.starts[p + 1]
            self.intervals.remove(self.starts[p + 1])
            self.starts.pop(p + 1)

        self.insert(start, end)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

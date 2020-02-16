"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Event:
    def __init__(self, time: int, start: bool):
        self.time = time
        self.start = start

    def __repr__(self): return str(self.time)

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Based on LeetCode's Solution 2
        # Greedy + Priority Queue
        # Time Complexity: O(I log N), I = number of intervals
        # Space Complexity: O(N)

        num_employee = len(schedule)
        breaks = []
        next_busy_pq = [(employee[0].start, ei, 0) for ei, employee in enumerate(schedule)]
        heapq.heapify(next_busy_pq)
        break_start = min(interval.start for employee in schedule for interval in employee)

        while len(next_busy_pq) > 0:
            t, eid, iid = heapq.heappop(next_busy_pq)
            if break_start < t:
                breaks.append(Interval(break_start, t))
            break_start = max(break_start, schedule[eid][iid].end)
            if iid + 1 < len(schedule[eid]):
                heapq.heappush(next_busy_pq, (schedule[eid][iid + 1].start, eid, iid + 1))
        return breaks

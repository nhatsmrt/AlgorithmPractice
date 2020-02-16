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
        # Time Complexity: O(I log I), I = number of intervals
        # Space Complexity: O(I)

        num_employee = len(schedule)

        events = []
        for employee in schedule:
            for interval in employee:
                events.append(Event(interval.start, True))
                events.append(Event(interval.end, False))
        events.sort(key=lambda e: e.time)
        print(events)

        num_working = 0
        i = 0
        break_start = -1
        breaks = []

        for event in events:
            if event.start:
                num_working += 1
                if break_start != - 1:
                    if event.time - break_start > 0:
                        breaks.append(Interval(break_start, event.time))
                    break_start = -1
            else:
                num_working -= 1
                if num_working == 0:
                    break_start = event.time

        return breaks

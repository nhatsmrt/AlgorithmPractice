class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(1)

        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        start = 0
        end = 0

        ret = 0

        while start < len(intervals):
            if end + 1 < len(intervals) and intervals[end + 1][1] <= intervals[start][1]:
                end += 1
            else:
                ret += 1
                start = end + 1

        return ret
        

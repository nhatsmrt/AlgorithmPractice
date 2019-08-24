class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if (len(intervals) <= 1): return 0

        intervals.sort(key=lambda interval: interval[1])
        curTime = intervals[0][1]
        ind = 1
        ret = 0

        while ind < len(intervals):
            if intervals[ind][0] < curTime:
                ret += 1
            else:
                curTime = intervals[ind][1]
            ind += 1

        return ret

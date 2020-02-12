class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ret = []
        for interval in intervals:
            if interval[1] < toBeRemoved[0] or interval[0] > toBeRemoved[1]:
                ret.append(interval)
            else:
                if interval[0] < toBeRemoved[0]:
                    ret.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1]:
                    ret.append([toBeRemoved[1], interval[1]])

        return ret

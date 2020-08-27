class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        ret = []

        intervals_with_ind = [(intervals[i][0], intervals[i][1], i) for i in range(len(intervals))]
        intervals_sorted_by_start = sorted(intervals_with_ind)

        for interval in intervals:
            end = interval[1]

            low = 0
            high = len(intervals) - 1

            while low < high:
                mid = low + (high - low) // 2

                if intervals_sorted_by_start[mid][0] < end:
                    low = mid + 1
                else:
                    high = mid

            if intervals_sorted_by_start[low][0] >= end:
                ret.append(intervals_sorted_by_start[low][2])
            else:
                ret.append(-1)

        return ret

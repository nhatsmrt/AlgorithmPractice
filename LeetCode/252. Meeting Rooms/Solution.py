class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time Complexity: O(n log n)
        # Space Complexity: O(1)

        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
        

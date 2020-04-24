class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Sort the jobs by date.
        # dp[i] = maximum profit from a subset of jobs[i:]
        # dp[i] = max(dp[i + 1], profit[i] + dp[k])
        # where k is the first job such that start[k] >= end[i]
        # (which can be found using binary search)


        # Time Complexity: O(n log n)
        # Space Complexity: O(n)


        jobs = [(start, end, prof) for start, end, prof in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda time:time[0])

        startTime = [job[0] for job in jobs]
        endTime = [job[1] for job in jobs]
        profit = [job[2] for job in jobs]


        self.dp = {}
        ret = self.maxProfit(startTime, endTime, profit, 0)
        return ret

    def maxProfit(self, startTime: List[int], endTime: List[int], profit: List[int], i: int) -> int:
        if i == len(startTime):
            return 0

        if i in self.dp:
            return self.dp[i]

        self.dp[i] = self.maxProfit(startTime, endTime, profit, i + 1)

        low = i + 1
        high = len(startTime)

        while low < high:
            mid = low + (high - low) // 2
            if startTime[mid] < endTime[i]:
                low = mid + 1
            else:
                high = mid

        if low == len(startTime) or (low < len(startTime) and startTime[low] >= endTime[i]):
            self.dp[i] = max(self.dp[i], profit[i] + self.maxProfit(startTime, endTime, profit, low))

        return self.dp[i]

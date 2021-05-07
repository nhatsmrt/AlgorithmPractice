class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Time Complexity: O(NK log N)
        # Space Complexity: O(NK)

        events.sort(key=lambda ev: (ev[0], ev[1]))
        self.dp = {}

        return self.maxSum(events, 0, k)


    def maxSum(self, events: List[List[int]], i: int, k: int):
        if i == len(events) or k == 0:
            return 0

        if (i, k) in self.dp:
            return self.dp[(i, k)]

        ret = events[i][-1]

        low = i + 1
        high = len(events)

        while low < high:
            mid = (low + high) // 2

            if events[mid][0] <= events[i][1]:
                low = mid + 1
            else:
                high = mid

        ret += self.maxSum(events, low, k - 1)
        ret = max(ret, self.maxSum(events, i + 1, k))

        self.dp[(i, k)] = ret
        return ret

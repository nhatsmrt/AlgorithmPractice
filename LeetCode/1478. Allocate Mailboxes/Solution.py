from itertools import accumulate


class Solution:
    INF = 1000000000

    def minDistance(self, houses: List[int], k: int) -> int:
        # Time Complexity: O(N log N K)
        # Space Complexity: O(NK)

        # dp[i][k] = min total dist when placing at most k mailboxes for houses for the house from 0 to i
        # ans = dp[len(houses) - 1][k]
        # dp[end][k] = min_i(
        #   dist_from_median(houses[i + 1],..., houses[end]) + dp[i][k - 1]
        #)

        # Let argmin[end][k] = arg min_i for dp[end][k]
        # then argmin[end][k] is monotonically non-decreasing w.r.t end
        # This suggests we can use Divide and Conquer Optimization

        houses.sort()
        self.prefix = list(accumulate(houses))

        self.dp = {}
        self.distFromMedianDP = {}

        for numMailBox in range(1, k + 1):
            self.findMinDist(houses, 0, len(houses) - 1, 0, len(houses) - 1, numMailBox)

        return self.dp[(len(houses) - 1, k)]

    def findMinDist(self, houses: List[int], start: int, end: int, argmin_low: int, argmin_high: int, numMailBox: int):
        # Compute dp[start][numMailBox], ..., dp[end][numMailBox]
        # knowing that the range of the argmins is [argmin_low, argmin_high]

        if start > end:
            return

        if numMailBox == 1:
            for i in range(len(houses)):
                self.dp[(i, 1)] = self.distFromMedian(houses, 0, i)
        else:

            if start == end:
                ret = self.INF
                key = (end, numMailBox)

                for i in range(argmin_low, argmin_high + 1):
                    cand = self.dp[(i, numMailBox - 1)]

                    if i < end:
                        cand += self.distFromMedian(houses, i + 1, end)

                    if cand < ret:
                        argmin = i
                        ret = cand

                self.dp[key] = ret
            else:
                ret = self.INF
                mid = (start + end) // 2
                key = (mid, numMailBox)

                for i in range(argmin_low, min(mid, argmin_high) + 1):
                    cand = self.dp[(i, numMailBox - 1)]
                    if i < mid:
                        cand += self.distFromMedian(houses, i + 1, mid)

                    if cand < ret:
                        argmin_mid = i
                        ret = cand

                self.dp[key] = ret

                self.findMinDist(houses, start, mid - 1, argmin_low, argmin_mid, numMailBox)
                self.findMinDist(houses, mid + 1, end, argmin_mid, argmin_high, numMailBox)

    def rangeSum(self, start, end):
        if start == 0:
            return self.prefix[end]

        return self.prefix[end] - self.prefix[start - 1]

    def distFromMedian(self, houses, start, end):
        # = sum(abs(houses[mid] - houses[i]))
        # = sum_{start <= i <= mid} houses(mid) - houses[i] + sum_{mid <= j <= end} houses[j] - houses[mid]
        # = houses[mid] * (mid - start + 1) - rangeSum(start, mid) - houses[mid] * (end - mid + 1) + rangeSum(mid, end)
        # = rangeSum(mid, end) - rangeSum(start, mid) - houses[mid] * (end + start - 2 * mid)

        key = (start, end)
        if key in self.distFromMedianDP:
            return self.distFromMedianDP[key]

        mid = (start + end) // 2
        ret = self.rangeSum(mid, end) - self.rangeSum(start, mid) - houses[mid] * (end + start - 2 * mid)

        self.distFromMedianDP[key] = ret
        return ret

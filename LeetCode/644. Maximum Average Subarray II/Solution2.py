from collections import deque


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Based on https://leetcode.com/problems/maximum-average-subarray-ii/discuss/105476/Python-Advanced-O(n)-solution-(Convex-Hull-Window)

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = sum(nums) / len(nums)
        high = max(nums)
        self.prefixes = [0]

        for num in nums:
            self.prefixes.append(num + self.prefixes[-1])

        # Observation 1: If we consider (i, prefixes[i]) as points in 2D plane,
        # then we are finding pair of points with maximum slope

        # Observation 2: If the end point is (end, prefixes[end]), then the points we need to consider
        # lie on the lower envelope of (0, prefixes[0]) to (j - k, prefixes[j - k])

        # Observation 3: If slope(hull[0], hull[1]) < slope(hull[0], hull[end]),
        # then slope(hull[1], hull[end]) > slope(hull[0], hull[end])

        # Observation 4: In the case described observation 3, we can safely discard hull[0]
        # (until the property no longer holds) and still ensures that the pair of points
        # with max slope is still considered

        hull = deque()
        ans = float('-inf')

        for end in range(k, len(self.prefixes)):
            # Add (end - k, prefixes[end - k]) to the lower envelope
            # while maintaining convexity:
            while len(hull) >= 2 and self.slope(hull[-1], hull[-2]) >= self.slope(hull[-1], end - k):
                hull.pop()
            hull.append(end - k)

            # Discarding extraneous points in the left of the lower envelope
            while len(hull) >= 2 and self.slope(hull[0], hull[1]) <= self.slope(hull[0], end):
                hull.popleft()

            ans = max(ans, self.slope(hull[0], end))

        return ans


    def slope(self, i: int, j: int) -> float:
        return (self.prefixes[j] - self.prefixes[i]) / (j - i)

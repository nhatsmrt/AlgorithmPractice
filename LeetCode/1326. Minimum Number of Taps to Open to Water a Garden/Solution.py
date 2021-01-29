class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # Idea: sort the intervals
        # then for each point to be covered, pick the interval covering it
        # extending as far to the right as possible

        ranges = map(lambda pair: (pair[0] - pair[1], pair[0] + pair[1]), enumerate(ranges))
        ranges = filter(lambda r: r[0] != r[1], ranges)
        ranges = sorted(ranges, key=lambda pair: -pair[0])

        ret = 0
        cur = 0

        while cur < n:
            while ranges and ranges[-1][0] <= cur and ranges[-1][1] < cur:
                ranges.pop()

            if not ranges or ranges[-1][0] > cur:
                # no interval covers cur:
                return -1

            ret += 1
            max_right = cur
            while ranges and ranges[-1][0] <= cur:
                max_right = max(ranges.pop()[1], max_right)

            cur = max_right

        return ret

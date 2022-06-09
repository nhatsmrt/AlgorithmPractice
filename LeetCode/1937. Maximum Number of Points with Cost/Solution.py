INF = 1000000000


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Time Complexity: O(MN)
        # Space Complexity: O(N)

        # cur[c] = max points obtained when reaching position c (of current row)
        cur = deepcopy(points[0])

        for r in range(1, len(points)):
            left = [0] * len(points[0])
            right = [0] * len(points[0])

            for c in range(len(points[0])):
                max_left = cur[c]

                if c > 0:
                    max_left = max(max_left, left[c - 1] - 1)

                left[c] = max_left

            for c in reversed(range(len(points[0]))):
                max_right = cur[c]

                if c < len(points[0]) - 1:
                    max_right = max(max_right, right[c + 1] - 1)

                right[c] = max_right

            cur = [0] * len(points[0])
            for c in range(len(points[0])):
                cur[c] = max(left[c], right[c]) + points[r][c]

        return max(cur)

def traverse(point1: List[int], point2: List[int]) -> int:
    dx, dy = abs(point1[0] - point2[0]), abs(point1[1] - point2[1])
    return max(dx, dy) # min(dx, dy) + max(dx, dy) - min(dx, dy)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ret = 0

        for i in range(len(points) - 1):
            ret += traverse(points[i], points[i + 1])

        return ret

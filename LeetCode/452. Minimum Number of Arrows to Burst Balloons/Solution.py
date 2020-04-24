class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the balloons by ending point
        # Repeatedly shoot the ballon with smallest ending point,
        # removing the ones it touches

        # Theorem: Given any set of remaining balloons
        # we can find a minimal set of shots
        # such that the first one is the greedy shot

        # Proof: Sort the optimal set of shots. If the first one
        # is after our greedy shot, then the first balloon is not shot down
        # If it's before our greedy shot, replace it with our greedy shot
        # still shots down at least as many balloons

        points.sort(key=lambda point: point[1])

        i = 0
        ret = 0

        while i < len(points):
            ret += 1

            j = i + 1
            while j < len(points) and points[i][1] >= points[j][0]:
                j += 1

            i = j

        return ret

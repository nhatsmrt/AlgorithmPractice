class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points_set = set()

        leftmost = 1000000000
        rightmost = -1000000000

        for point in points:
            leftmost = min(leftmost, point[0])
            rightmost = max(rightmost, point[0])
            points_set.add((point[0], point[1]))

        mid = (leftmost + rightmost) / 2
        for point in points:
            if (2 * mid - point[0], point[1]) not in points_set:
                return False

        return True
        

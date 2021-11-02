def area(points: List[List[int]]) -> int: # shoelace formula
    fst = sum(points[i][0] * points[(i + 1) % len(points)][1] for i in range(len(points)))
    snd = sum(points[i][1] * points[(i + 1) % len(points)][0] for i in range(len(points)))

    return 0.5 * abs(fst - snd)

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Time and Space Complexity: O(1)
        return area(points) > 0

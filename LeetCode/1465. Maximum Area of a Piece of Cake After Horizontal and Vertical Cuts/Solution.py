class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Time Complexity: O(M log M + N log N)
        # Space Complexity: O(1)

        horizontalCuts.append(h)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        dx = horizontalCuts[0]

        for i in range(1, len(horizontalCuts)):
            dx = max(dx, horizontalCuts[i] - horizontalCuts[i - 1])

        dy = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            dy = max(dy, verticalCuts[i] - verticalCuts[i - 1])

        return dx * dy % 1000000007

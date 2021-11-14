class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Time and Space Complexity: O(N)

        ret = []
        stack = []

        for height in heights[::-1]:
            can_see = 0

            while stack and stack[-1] < height:
                can_see += 1
                stack.pop()

            if stack:
                can_see += 1

            ret.append(can_see)
            stack.append(height)

        return ret[::-1]

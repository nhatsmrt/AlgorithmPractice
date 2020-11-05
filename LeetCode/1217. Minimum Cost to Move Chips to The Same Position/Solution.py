class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        evens = len(list(filter(lambda pos: pos % 2 == 0, position)))
        odds = len(list(filter(lambda pos: pos % 2 == 1, position)))

        return min(evens, odds)

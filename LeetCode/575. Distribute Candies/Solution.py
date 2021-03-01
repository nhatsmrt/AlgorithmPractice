class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Time and Space Complexity: O(N)
        return min(len(candyType) // 2, len(set(candyType)))

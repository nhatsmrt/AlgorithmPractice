class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        min_val = min(nums)
        return sum(map(lambda val: val - min_val, nums))

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        numsum = sum(nums)
        delta = abs(goal - numsum)

        return math.ceil(delta / limit)

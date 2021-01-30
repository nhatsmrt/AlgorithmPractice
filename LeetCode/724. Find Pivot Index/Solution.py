class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        cumsum = 0
        total_sum = sum(nums)

        for i, num in enumerate(nums):
            if cumsum == total_sum - num - cumsum:
                return i
            cumsum += num

        return -1

from typing import List, Tuple


class Solution:
    # Time Complexity: O(n log((MAX_VAL - MEAN_VAL) / eps))
    # Space Complexity: O(n)

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = sum(nums) / len(nums)
        high = max(nums)
        self.prefixes = [0] * (len(nums) + 1)

        eps = 1e-6

        while low < high - eps:
            mid = (low + high) / 2

            if self.possible(nums, mid, k):
                low = mid
            else:
                high = mid

        return low

    def possible(self, nums: List[int], target: float, k: int) -> bool:
        for i in range(0, len(nums)):
            self.prefixes[i + 1] = self.prefixes[i] + nums[i] - target

        lower = 100000000
        for i in range(k, len(self.prefixes)):
            lower = min(lower, self.prefixes[i - k])
            if self.prefixes[i] > lower:
                return True

        return False

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target) # exclusive

        return end - start > len(nums) / 2

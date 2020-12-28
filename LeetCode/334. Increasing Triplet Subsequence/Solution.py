class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Time complexity: O(N)
        # Space complexity: O(1)

        if len(nums) < 3:
            return False

        first = 1000000000000
        second = 1000000000000

        for num in nums:
            if num < first:
                first = num
            elif num < second and num > first:
                second = num
            elif num > second:
                return True

        return False

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == mid:
                low = mid + 1
            else:
                high = mid

        if nums[low] != low:
            return low

        return len(nums)

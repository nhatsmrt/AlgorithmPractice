class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums)


        while low + 1 < high:
            mid = low + (high -  low) // 2

            num_missing = nums[mid] - nums[low] + low - mid
            if num_missing >= k:
                high = mid
            else:
                low = mid
                k -= num_missing

        return nums[low] + k

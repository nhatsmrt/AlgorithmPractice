class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = 1

        start = 0
        end = 0

        while start < len(nums):
            if end + 1 < len(nums) and nums[end + 1] > nums[end]:
                end += 1
            else:
                ret = max(ret, end - start + 1)
                start = end + 1
                end += 1

        return ret

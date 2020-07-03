class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0

        while start < len(nums) and nums[start] == 0 and (start + 1 == len(nums) or nums[start + 1] == 0):
            start += 1
        if start == len(nums):
            return 0

        zero_ind = start if (nums[start] == 0) else -1
        end = start + 1
        max_len = zero_ind + 1

        while end < len(nums):
            if nums[end] == 0:
                if zero_ind != -1:
                    # update max_len:
                    max_len = max(max_len, end - start - 1)
                    # reset:
                    start = zero_ind + 1

                zero_ind = end
            end += 1

        return max(max_len, end - start - 1)
        

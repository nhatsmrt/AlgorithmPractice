class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # Time Complexity: O(n), Space Complexity: O(1)

        cur_sum = 0
        start = 0
        end = 0
        ret = 0

        while start < len(nums):
            while end < len(nums) and cur_sum < s:
                cur_sum += nums[end]
                end += 1

            if cur_sum < s:
                break
            else:
                length = end - start
                ret = length if ret == 0 else min(ret, length)

                cur_sum -= nums[start]
                start += 1
                end = max(start, end)

        return ret
